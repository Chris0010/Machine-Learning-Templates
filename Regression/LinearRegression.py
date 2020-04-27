# Simple Linear Regression & Multiple Linear Regression

# Simple Linear Regression and Multiple Linear Regression both use the same sklearn tool, in the event MLR has categorical variables changes will need to be made to RegressionTemplate to fit those categorical variables to dummy variables
# Fitting Linear Regression to the Training set
# import variables from RegressionTemplate
from RegressionTemplate import X_train, y_train, X_test, y_test
# call linear regression tool from sklearn, for multiple linear regression the tool automatically avoid the dummy variable trap and scale your variables, also backward elimination technique is automatically done by the LinearRegression class in sklearn
from sklearn.linear_model import LinearRegression
# assign the regressor for linear regression
regressor = LinearRegression()
# fit the regressor
regressor.fit(X_train, y_train)
# make sure to choose the correct predict code in Predict_Visualize_Regression