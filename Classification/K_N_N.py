# K-Nearest Neighbors

# import variables from classificationtemplate
from classificationtemplate import X_train, y_train
# fix the y_train data's dimensionality to fit with the X_train data's dimensionality
y_train = y_train.ravel()
# import the K-NN classifier from sklearn
from sklearn.neighbors import KNeighborsClassifier
# assign the classification for K-Nearest neighbor with n=5, metric minkowski, and p=2
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
# fit the classifier to the training set
classifier.fit(X_train, y_train)
