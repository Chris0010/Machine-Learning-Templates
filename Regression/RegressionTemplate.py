# Regression Template

# Importing the libraries
import pandas as pd
import numpy as np

# Importing the dataset
dataset = pd.read_csv()
X =
y =

'''
# Encoding categorical data
from sklearn.preprocessing import  OneHotEncoder
from sklearn.compose import ColumnTransformer
# in the brackets you will specify what column index needs to be onehotencoded
ct = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X), dtype = np.float)

# Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
'''