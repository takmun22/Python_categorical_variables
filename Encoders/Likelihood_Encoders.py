###Mean encoding variables####

#Import the required packages
import numpy as np
import pandas as pd
import itertools
from tqdm import tqdm
from sklearn.model_selection import StratifiedKFold



#Save the iterator function from itertools in a shorter name
def likelihood_encoder(dataset,categorical_variables,response_variable,nfolds=5,seed=np.random.rand()*100):
  
  """
  
  dataset: Has to be PandasDataFrame which has all the categorical variables and the response variable.
  
  categorical_variables: Has to be a Python list containing all the names of the categorical variables.
  
  response_variable: Has to be the name of the response variable in string format.
  
  """

  #Print the number of features #
  print(" There are {} categorical features".format(len(categorical_variables)))

  #Make a stratified k-fold generator to split the data into the required number of folds
  kfold = StratifiedKFold(n_splits=nfolds,random_state=seed, shuffle=True)

  #Make a dictionary to store final_results
  storage_for_values= dict()

  final_dataset = dataset.copy()

  for train_index,valid_index in tqdm(kfold.split(dataset, dataset[response_variable])):
    #make the dataset which will be used to extract averages for each level in each categorical variable
    train_data = dataset.loc[train_index]

    #make the dataset with the remaining portion of the data where we will apply the averages to each category
    valid_data = dataset.loc[valid_index]

    storage_for_everything = dict()

    for i in iter(categorical_variables):
      #Pick which variable is in play
      cat_var = i 

      #Select a column from the categorical variables , get an average of each value
      average_response = train_data[[i,response_variable]].groupby(by = cat_var).mean()[response_variable]

      #Seperarte the index and values
      index = average_response.index
      values = average_response.values

      #Make a dictionary with all the values
      temp_storage = {index[k]:values[k] for  k in range(len(index))}

      #Store all the values for this variable in the overall dictionary
      storage_for_everything[i] = temp_storage

      #Make a dictionary to store the numeric output for the next loop
      store = dict()

    #Loop through the variables again
    for j in iter(categorical_variables):
        
        #Select relevant dictonary
        rel_dic = storage_for_everything[j]

        #Map to the relevant data
        output = valid_data[j].map(lambda x:rel_dic[x]).values

        store[j] = output

    #Store the values for this run
    storage_for_values[tuple(valid_index)] = store

  #Return the final dictionary with the values for each variable
  return storage_for_values
