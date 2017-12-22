#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC

classifier = SVC(kernel='rbf', C=10000)
print classifier
print classifier.kernel
t0 = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
prediction = classifier.predict(features_test)
print "training time:", round(time() - t0, 3), "s"

print prediction[10], prediction[26], prediction[50]
print "Chris:", list(prediction).count(1)

from sklearn.metrics import accuracy_score
print accuracy_score(labels_test, prediction)
