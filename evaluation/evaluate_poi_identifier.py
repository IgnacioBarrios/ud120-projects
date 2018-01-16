#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import tree
from sklearn import cross_validation 
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size = 0.3, random_state=42)

Tree = tree.DecisionTreeClassifier()
Tree = Tree.fit(features_train, labels_train)
acc_ = Tree.score(features_test, labels_test)

print "Accuracy 30% train data: ", round(acc_,3)

# Quiz 28:  Number Of POIs In Test Set: 4

print "Number Of POIs In Test Set: ", sum(labels_test)

# Quiz 29: Quiz: Number Of People In Test Set: 29

print "Number Of People In Test Set: ", len(labels_test)

# Quiz 30: Accuracy Of A Biased Identifier (all 0) --> 0.862

print "Accuracy Of A Biased Identifier: ", ((29-4)/29.)

# Quiz 31: Number Of True Positives --> 0
from sklearn.metrics import confusion_matrix
y_true = labels_test
y_pred = Tree.predict(features_test)

matrix = confusion_matrix(y_true, y_pred)
print "Number Of True Positives: ", matrix[1,1]

# Quiz 32: Percision Of Your POI Identifier ---> 0

from sklearn.metrics import precision_score
print "Percision Of Your POI Identifier: ", precision_score(y_true, y_pred) 

# Quiz 33: Recall Of Your POI Identifier ---> 0
from sklearn.metrics import recall_score
print "Recall Of Your POI Identifier: ", recall_score(y_true, y_pred) 

# Quiz 34: How Many True Positives? ---> 6

y_pred = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
y_true = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

matrix = confusion_matrix(y_true, y_pred)
print "Number Of True Positives: ", matrix[1,1]

# Quiz 35: How Many True Negatives? ---> 9
print "Number Of True Negatives: ", matrix[0,0]

# Quiz 36: How Many False Positives? ---> 3
print "Number Of False Positives: ", matrix[0,1]

# Quiz 37: How Many False Negatives? ---> 3
print "Number Of False Negatives: ", matrix[1,0]

# Quiz 38: Precision? ---> 0.667
print "Precision: ", precision_score(y_true, y_pred) 

# Quiz 39: Recall? ---> 0.75
print "Recall: ", recall_score(y_true, y_pred) 

# Quiz 40: Quiz: Making Sense Of Metrics 1? ---> 0.75

