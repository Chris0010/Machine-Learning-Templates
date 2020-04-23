# Logistic Regression

# import variables from classificationtemplate
from classificationtemplate import X_train, y_train
# import the logistic regression classifier from sklearn
from sklearn.linear_model import LogisticRegression
# assign the classification for logistic regression
classifier = LogisticRegression()
# fit the classifier to the training set
classifier.fit(X_train, y_train)
