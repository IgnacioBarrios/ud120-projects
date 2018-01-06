#!/usr/bin/python

""" lecture and example code for KNeighborsClassifier """

import sys
sys.path.append("../choose_your_own/")
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()


from sklearn.neighbors import KNeighborsClassifier

### create classifier
clf = KNeighborsClassifier(n_neighbors=3)

### use the trained classifier to predict labels for the test features
clf.fit(features_train, labels_train)

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())


# Accuracy
accuracy = clf.score(features_test, labels_test)
print "accuracy: ", round(accuracy*100,2)

"""
                Accuracy
Naive bayes     88.4% 
SVM             92%
Decision trees  91.2%
Kneighbour (5)  92 %
Kneighbour (3)  93.6 %
Kneighbour (1)  94 %
AdaBoost:       92.4%
RandomForest    92%
RandomForest(1) 93.2%
"""