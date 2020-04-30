# Support Vector Regression

# import variables from RegressionTemplate
from RegressionTemplate import X_train, y_train, X_test, y_test
# Feature scaling is necessary
y_train = y_train.reshape(len(y_train), 1)
y_test = y_test.reshape(len(y_test), 1)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
y_train = sc_y.fit_transform(y_train)

# call SVR from sklearn
from sklearn.svm import SVR
# assign the regressor for SVR
regressor = SVR(kernel = 'rbf')
# train on the data
regressor.fit(X_train, y_train.ravel())
