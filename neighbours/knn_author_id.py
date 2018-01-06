#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 4 (k nearest neighbours) 
    mini-project.

    Use a k nearest neighbours to identify emails from the Enron corpus by author:    
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
from sklearn.neighbors import KNeighborsRegressor

### create classifier
clf = KNeighborsRegressor(n_neighbors=2)

### fit the classifier on the training features and labels
#To have smaller training dataset (1 is 100%, 10 is 10%, 100 is 1%)
train_adjustment= 1
features_train = features_train[:len(features_train)/train_adjustment] 
labels_train = labels_train[:len(labels_train)/train_adjustment] 

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
t0 = time()
accuracy = clf.score(features_test, labels_test)
print "accuracy NearestNeighbors: ",accuracy, " . Time:", round(time()-t0, 3), "s"



#########################################################
# K-neigbours           5       2
# Training Time(s)   8.828      8.702
# Predict Time(s)    349.814    231.024
# Accuracy Time(s)   mucho      229.809 
# Accuracy           0.599      0.818