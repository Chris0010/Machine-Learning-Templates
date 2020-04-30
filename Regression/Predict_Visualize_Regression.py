# Predict and Visualize results

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Fitting regression to the training set import the variables and necessary regressor tool
R2_list = {}
# Predictors

from LinearRegression import regressor, X_train, y_train, X_test, y_test
# Predicting the Test set results (Simple Linear Regression)
y_pred = regressor.predict(X_test)


# Predicting the Test set results (Multiple Linear Regression) add this:
# limit numerical values to two decimal places
np.set_printoptions(precision = 2)
# print the result of concatenated vector of predicted and vector of actual
print("Predicted values, Test values: ", np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Determine R2
from sklearn.metrics import r2_score
Linear_R2 = r2_score(y_test, y_pred)
print("R squared: ", Linear_R2)
R2_list.update(LinearRegression = Linear_R2)

# Predicting the results with Polynomial Regression
from PolynomialRegression import regressor, poly_reg, X_test, y_test
y_pred = regressor.predict(poly_reg.fit_transform(X_test))
print(y_pred)

# Determine R2
from sklearn.metrics import r2_score
Poly_R2 = r2_score(y_test, y_pred)
print("R squared: ", Poly_R2)
R2_list.update(PolynomialRegression = Poly_R2)

# Predicting the results with SVR
from SVR import regressor, sc_X, sc_y, X_train, y_train, X_test, y_test
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(X_test)))
# limit numerical values to two decimal places
np.set_printoptions(precision = 2)
# print the result of concatenated vector of predicted and vector of actual
print("Predicted values, Test values: ", np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

from sklearn.metrics import r2_score
SVR_R2 = r2_score(y_test, y_pred)
print("R squared: ", SVR_R2)
R2_list.update(SVR = SVR_R2)

# Predicting the results with the Decision tree regressor
from DecisionTreeRegression import regressor, X_train, y_train, X_test, y_test
y_pred = regressor.predict(X_test)
# limit numerical values to two decimal places
np.set_printoptions(precision = 2)
# print the result of concatenated vector of predicted and vector of actual
print("Predicted values, Test values: ", np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

from sklearn.metrics import r2_score
DecisionTree_R2 = r2_score(y_test, y_pred)
print("R squared: ", DecisionTree_R2)
R2_list.update(DecisionTree = DecisionTree_R2)

# Predicting the results with the random forest regressor
from RandomForestRegression import regressor, X_train, y_train, X_test, y_test
y_pred = regressor.predict(X_test)
# limit numerical values to two decimal places
np.set_printoptions(precision = 2)
# print the result of concatenated vector of predicted and vector of actual
print("Predicted values, Test values: ", np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

from sklearn.metrics import r2_score
RandomForest_R2 = r2_score(y_test, y_pred)
print("R squared: ", RandomForest_R2)
R2_list.update(RandomForest = RandomForest_R2)

# select the best regression model
import operator
print(R2_list)
print("\n\nThe best regression model is ", max(R2_list.items(), key = operator.itemgetter(1))[0])

'''
# Visualization plots
# Visualizing the Training set results (Simple Linear Regression)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('(Training Set)')
plt.xlabel('')
plt.ylabel('')
plt.show()

# Visualizing the Test set results (Simple Linear Regression)
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('(Test Set)')
plt.xlabel('')
plt.ylabel('')
plt.show()
'''
'''
# Visualizing Linear Regression results (Polynomial)
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()

# Visualizing Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
'''
'''
# Visualizing SVR results
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color = 'blue')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
'''
'''
# Visualizing the decision tree regressor
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
'''
'''
# Visualizing the random forest regressor
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
'''