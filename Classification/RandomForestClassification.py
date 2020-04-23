# Random forest classification

# import variables from classificationtemplate
from classificationtemplate import X_train, y_train
# import random forest classifier from sklearn
from sklearn.ensemble import RandomForestClassifier
# assign the classifier to random forest
# n_estimators is how many trees you want
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')
# fit the classifier to the training set
classifier.fit(X_train, y_train)
