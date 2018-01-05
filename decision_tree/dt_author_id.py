#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn import tree

### create classifier
clf = tree.DecisionTreeClassifier(min_samples_split=40)

### fit the classifier on the training features and labels
t0 = time()
clf = clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

### calculate and return the accuracy on the test data
### this is slightly different than the example, 
### where we just print the accuracy
### you might need to import an sklearn module
accuracy = clf.score(features_test, labels_test)
print "accuracy 1: ",accuracy



#########################################################
# Samples Split     50  
# Accuracy          0.978
# Training Time(s)   92
# Predict Time(s)    0.072  

# How many features are in the data: 
# 3785 (percentile 10), 
# 379 (percentile 1)
# Percentile is changed in email_preprocess
print 'Number of features: ', len(features_train[0])
