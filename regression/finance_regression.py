#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature

features_list = ["bonus", "long_term_incentive"]
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

from sklearn.linear_model import LinearRegression

### name your regression reg
reg = LinearRegression()
    
### your code goes here!
reg.fit (feature_train, target_train)
    
print "Slope: ", reg.coef_
print "Intercept: ", reg.intercept_
print "Accuracy Training data: ", reg.score(feature_train, target_train)
print "Accuracy Test Data: ", reg.score(feature_test, target_test)

"""
features_list = ["bonus", "salary"]
Slope:  [ 5.44814029]
Intercept:  -102360.543294
Accuracy Training data:  0.0455091926995
Accuracy Test Data:  -1.48499241737

features_list = ["bonus", "long_term_incentive"]
Slope:  [ 1.19214699]
Intercept:  554478.756215
Accuracy Training data:  0.217085971258
Accuracy Test Data:  -0.59271289995

"""

### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
plt.xlabel(features_list[1])

# Added to see the effect of removing outliers
reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b") 
print "Slope: ", reg.coef_
print "Intercept: ", reg.intercept_
print "Accuracy Training data: ", reg.score(feature_train, target_train)
print "Accuracy Test Data: ", reg.score(feature_test, target_test)


plt.ylabel(features_list[0])
plt.legend()
plt.show()
