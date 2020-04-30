# Polynomial regression

# import variables from classificationtemplate
from RegressionTemplate import X_train, y_train, X_test, y_test
# call linear regression tool from sklearn
from sklearn.linear_model import LinearRegression
# call polynomial features
from sklearn.preprocessing import PolynomialFeatures
# assign the polynomial features and choose what level of polynomial to go to
poly_reg = PolynomialFeatures(degree = 4)
# fit and transform the polynomials
X_poly = poly_reg.fit_transform(X_train)
# assign the regressor for new linear regression model with polynomials# assign the regressor for linear regression
regressor = LinearRegression()
# # fit the regressor to the data
regressor.fit(X_poly, y_train)


