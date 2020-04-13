# Scaling Features and Splitting Data Into Training and Testing Sets

# using the coded data from Categorical_Data_Coding file, to see how to encode the data please see Categorical_Data_Coding.py
import pandas as pd
# the feature scaling is dependent upon the X values being correct, this is inherently dependent upon project so the below code is meant as an example only and the feature scaling code is interchangeable
dataset = pd.read_csv('RandomMixedDataframe.csv')
dataset = dataset.join(pd.DataFrame(data = {'E': ['yes', 'no', 'yes', 'yes', 'no']}))
X = dataset.iloc[:, 1:5].values
y = dataset.iloc[:, -1].values
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [2])], remainder ='passthrough')
X = ct.fit_transform(X)
X = pd.DataFrame(X)
X = X.iloc[:, :-2].values
le = LabelEncoder()
y = le.fit_transform(y)

# feature scaling the independent variables to avoid skewing results in favor of feature with higher variance (see further explanation file)
from sklearn.preprocessing import StandardScaler
# assigning class for scaling to unit variance
sc = StandardScaler()
# fitting to independent variables, all independent variables must be present with dependent variable removed
X = sc.fit_transform(X)

# independent variables (X) and dependent variable (y) are split into training and testing sets (see further explanation file)
from sklearn.model_selection import train_test_split
# this is a small dataset and would never be split, but is being used as an example and such the test_size would likely never be set to 0.4
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 0)
