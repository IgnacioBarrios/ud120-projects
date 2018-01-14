# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 22:23:46 2018

@author: CASA
"""

#!/usr/bin/python

""" 
PLEASE NOTE:
The api of train_test_split changed and moved from sklearn.cross_validation to
sklearn.model_selection(version update from 0.17 to 0.18)

The correct documentation for this quiz is here: 
http://scikit-learn.org/0.17/modules/cross_validation.html
"""

from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
features = iris.data
labels = iris.target

###############################################################
### YOUR CODE HERE
###############################################################

### import the relevant code and make your train/test split
### name the output datasets features_train, features_test,
### labels_train, and labels_test
# PLEASE NOTE: The import here changes depending on your version of sklearn
from sklearn import cross_validation # for version 0.17
# For version 0.18
# from sklearn.model_selection import train_test_split



### set the random_state to 0 and the test_size to 0.4 so
### we can exactly check your result
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size = 0.4, random_state=0)

###############################################################
# DONT CHANGE ANYTHING HERE
clf = SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)

print clf.score(features_test, labels_test)
##############################################################
def submitAcc():
    return clf.score(features_test, labels_test)
