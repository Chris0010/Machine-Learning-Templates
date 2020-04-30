# Random Forest Regression

# import variables from RegressionTemplate
from RegressionTemplate import X_train, y_train, X_test, y_test
# call decision tree tool from sklearn
from sklearn.ensemble import RandomForestRegressor
# assign regressor for decision tree, n_estimators is the number of trees in the forest it defaults to 100
regressor = RandomForestRegressor(n_estimators = 10, random_state=0)
# fit the regressor to the data
regressor.fit(X_train, y_train)