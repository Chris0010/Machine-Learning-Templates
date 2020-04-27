# Predict and Visualize results

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Fitting regression to the training set
# import the variables and necessary regressor tool
# from LinearRegression import regressor, X_train, y_train, X_test, y_test
# from PolynomialRegression import lin_reg, poly_reg, lin_reg_2, X, y
#from SVR import regressor, sc_X, sc_y, X, y
'''
# Predicting the Test set results (Simple Linear Regression)
y_pred = regressor.predict(X_test)
print(y_pred)


# Predicting the Test set results (Multiple Linear Regression) add this:
# limit numerical values to two decimal places
np.set_printoptions(precision = 2)
# print the result of concatenated vector of predicted and vector of actual
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))
'''
'''
# Predicting the results with Polynomial Regression
# double brackets for 2D prediction
X_pred = lin_reg_2.predict(poly_reg.fit_transform([[]]))
print(X_pred)
'''
'''
X_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform([[]])))
print(X_pred)
'''
'''
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