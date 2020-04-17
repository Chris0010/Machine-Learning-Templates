# K-Nearest Neighbors

from classificationtemplate import X_train, y_train
y_train = y_train.ravel()
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)
