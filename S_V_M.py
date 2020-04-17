# Support Vector Machines

# import variables from classificationtemplate
from classificationtemplate import X_train, y_train
# import the SVM classifier from sklearn
from sklearn.svm import SVC
'''
kernels:
the default kernel is 'rbf' which is the Gaussian kernel or radial base function (rbf)
the sigmoid kernel is directional and makes a yes or no type decision available
assign the classification support vector machine with a linear kernel to get a similar result to logistic regression
polynomial kernel is another choice similar to linear classification the same way linear and polynomial regression are similar
from the literature: kernel – Specifies the kernel type to be used in the algorithm. It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or a callable. If none is given, 'rbf' will be used. If a callable is given it is used to pre-compute the kernel matrix from data matrices; that matrix should be an array of shape ``(n_samples, n_samples)``.
'''
classifier = SVC(kernel = 'rbf')
# fit the classifier to the training set
classifier.fit(X_train, y_train)