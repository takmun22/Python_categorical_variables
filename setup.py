import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Tak_Mun",
    version="0.0.1",
    author="Tak Mun",
    description="A package to do complete miscellaneous acts on categorical data",
    url="https://github.com/takmun22/categorical_variables",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
