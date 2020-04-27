# Polynomial regression

# import variables from classificationtemplate
from RegressionTemplate import X, y
# call linear regression tool from sklearn
from sklearn.linear_model import LinearRegression
X = X.reshape(-1, 1)
# assign the regressor for linear regression
lin_reg = LinearRegression()
# fit the regressor to the data
lin_reg.fit(X, y)
# call polynomial features
from sklearn.preprocessing import PolynomialFeatures
# assign the polynomial features and choose what level of polynomial to go to
poly_reg = PolynomialFeatures(degree = 2)
# fit and transform the polynomials
X_poly = poly_reg.fit_transform(X)
# assign the regressor for new linear regression model with polynomials
lin_reg_2 = LinearRegression()
# fit the new regressor to the data
lin_reg_2.fit(X_poly, y)


