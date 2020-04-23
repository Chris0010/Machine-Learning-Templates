# Decision tree classification

# import variables from classificationtemplate
from classificationtemplate import X_train, y_train
# import the decision tree classifier from sklearn
from sklearn.tree import DecisionTreeClassifier
# assign the classifier to decision tree classifier
classifier = DecisionTreeClassifier()
# fit the classifier to the training set
classifier.fit(X_train, y_train)
