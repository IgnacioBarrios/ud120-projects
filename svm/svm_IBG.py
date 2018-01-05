#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC

### create classifier
clf = SVC(kernel="linear")

"""
C = 1 is por defecto

Con train_adjustment= 100 (1%)
            C=1,10,100  1000  10000
Train time  0.3
Pred Time   2.3
Accuracy    0.616       0.821  0.8925     

Con train_adjustment= 1 (100%) C = 10000
Train time  208
Pred Time   19.7
Accuracy    0.9908
"""
clf = SVC(C=10000.0, kernel='rbf')


### fit the classifier on the training features and labels
t0 = time()

#To have smaller training dataset
train_adjustment= 1
features_train = features_train[:len(features_train)/train_adjustment] 
labels_train = labels_train[:len(labels_train)/train_adjustment] 

clf.fit(features_train, labels_train)
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
print "accuracy SVC 1- Lineal: ",accuracy

# Other way:
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "accuracy SVC 2 - Lineal: ", accuracy


#########################################################
# Cuantos son del grup de Chris (1)
sum(pred == 1)


