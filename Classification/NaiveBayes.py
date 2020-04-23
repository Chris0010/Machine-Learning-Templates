# Naive Bayes

# import variables from classificationtemplate
from classificationtemplate import X_train, y_train
# import the naive bayes classifier from sklearn
from sklearn.naive_bayes import GaussianNB
# assign the classifier to Naive Bayes
classifier = GaussianNB()
# fit the classifier to the training set
classifier.fit(X_train, y_train)
