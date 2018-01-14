#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

### your code goes here

from sklearn import tree
clf_2 = tree.DecisionTreeClassifier(min_samples_split=2)

clf_2 = tree.DecisionTreeClassifier()
clf_2 = clf_2.fit(features_train, labels_train)

acc_train_min_samples_split_2 = clf_2.score(features_train, labels_train)
acc_test_min_samples_split_2 = clf_2.score(features_test, labels_test)

print "acc_train_min_samples_split_2: ", round(acc_train_min_samples_split_2,3)
print "acc_test_min_samples_split_2: ", round(acc_test_min_samples_split_2,3)


### Identify the Most Powerful Features

importances = clf_2.feature_importances_

indices = numpy.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

#for f in range(X.shape[1]):
for f in range(0,10):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

### Get The Most Important Word
list_words = vectorizer.get_feature_names()

for f in range(0,10):
    i = indices[f]
    print("%d. feature %d (%f) Word %s" % (f + 1, i, importances[i], list_words[i]))

