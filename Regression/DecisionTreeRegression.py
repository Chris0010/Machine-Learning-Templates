# Decision Tree Regression

# import variables from RegressionTemplate
from RegressionTemplate import X_train, y_train, X_test, y_test
# call decision tree tool from sklearn
from sklearn.tree import DecisionTreeRegressor
# assign regressor for decision tree
regressor = DecisionTreeRegressor(random_state=0)
# fit the regressor to the data
regressor.fit(X_train, y_train)
