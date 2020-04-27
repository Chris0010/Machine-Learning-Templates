# Support Vector Regression

# import variables from RegressionTemplate
from RegressionTemplate import X, y
# Feature scaling is necessary
X = X.reshape(len(X), 1)
y = y.reshape(len(y), 1)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# call SVR from sklearn
from sklearn.svm import SVR
# assign the regressor for SVR
regressor = SVR(kernel = 'rbf')
# train on the data
regressor.fit(X, y.ravel())
