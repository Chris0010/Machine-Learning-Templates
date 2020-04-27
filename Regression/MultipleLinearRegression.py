# Multiple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv()
X =
y =

# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X), dtype = np.float)

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size = 0.2)

# Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Set Results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.regression.linear_model as lm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = lm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())

# Remove X_opt[2]
X_opt_2 = X_opt[:, [0, 1, 3, 4, 5]]
regressor_OLS_2 = lm.OLS(endog = y, exog = X_opt_2).fit()
print(regressor_OLS_2.summary())

# Remove X_opt_2[1]
X_opt_3 = X_opt_2[:, [0, 2, 3, 4]]
regressor_OLS_3 = lm.OLS(endog = y, exog = X_opt_3).fit()
print(regressor_OLS_3.summary())

# Remove X_opt_3[2]
X_opt_4 = X_opt_3[:, [0, 1, 3]]
regressor_OLS_4 = lm.OLS(endog = y, exog = X_opt_4).fit()
print(regressor_OLS_4.summary())

# Remove X_opt_4[2]
X_opt_5 = X_opt_4[:, [0, 1]]
regressor_OLS_5 = lm.OLS(endog = y, exog = X_opt_5).fit()
print(regressor_OLS_5.summary())
print(X_opt_5)