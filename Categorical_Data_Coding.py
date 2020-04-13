# Coding Categorical Data

# import the pandas library
import pandas as pd

# import the dataset with mixed datatypes to be used to demonstrate variable transformation
dataset = pd.read_csv('RandomMixedDataframe.csv')
dataset = dataset.join(pd.DataFrame(data = {'E': ['yes', 'no', 'yes', 'yes', 'no']}))
# arbitrarily select columns for independent variables (for the sake of example; no analysis is to be run on this data)
X = dataset.iloc[:, 1:5].values
# selecting a categorical dependent variable
y = dataset.iloc[:, -1].values

# encoding the independent variable to be expressed as onehotencoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# set up column transformer to enable the categorical variable to be changed into multiple columns without changing the other data columns
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [2])], remainder ='passthrough')
X = ct.fit_transform(X)
# Keep in mind this pushes the transformed column (now columns) to the front of the data

# encoding the dependent variable (best for binary answers e.g. yes/no)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
# if at any point you cannot remember what each dummy variable stands for run the following to transform the variables back: y = le.inverse_transform(y)

