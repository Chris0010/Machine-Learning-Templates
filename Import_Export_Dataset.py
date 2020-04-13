# Importing data

## set path
# import os
# os.chdir()

# Import necessary libraries
import pandas as pd
import numpy as np

# Import dataset
dataset = pd.read_csv(r'RandomMissingDataframe.csv')

# Define columns to be used as independent variables
X = dataset.iloc[:, 2:5]

# Define column with dependent variable
y = dataset.iloc[:, 1]

# to combine two dataframes
newdataset = X.join(y)

# adding new data to old data
adddataset = dataset.append(dataset)

# Filling in missing data values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X)
X = imputer.transform(X)
X = pd.DataFrame.from_records(X)

## export to a .csv
# newdataset.to_csv(r'newRandomDataframe.csv', index = False)


