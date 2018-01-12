#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
#feature_2 = "restricted_stock"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(data)
pred = kmeans.predict(data)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

# QUIZ 21 Add new feature
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"

features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(data)
pred = kmeans.predict(data)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters3.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

# QUIZ 21 Stock Option Range

def MinMaxArray(data_dict, Field):
    
    min_val = 1e130
    max_val = 0
    
    for field in data_dict:
        val = data_dict[field][Field]
    
        if val > max_val and val != "NaN":
            max_val = val
    
        if val < min_val and val != "NaN":
            min_val = val        
            
    print "Min/max value of ", Field, "is: ", min_val, max_val
     
    return min_val, max_val

min_stock, max_stock = MinMaxArray(data_dict, "exercised_stock_options")
  

# QUIZ 22 Salary Range: 1111258 477


min_salary, max_salary = MinMaxArray(data_dict, "salary")
  


"""
Quiz - 1 16: Computing Rescaled Features

"""

print "Salary 200k€: ", featureScaling_value(2e5, min_salary, max_salary)
print "Stock options 1M€: ", featureScaling_value(1e6, min_stock, max_stock)


feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"

features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
rescaled_data = scaler.fit_transform(data)


poi, finance_features = targetFeatureSplit( rescaled_data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(data)
pred = kmeans.predict(data)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"


# QUIZ 17 Salary and from_messages: 1111258 477

min_salary, max_salary = MinMaxArray(data_dict, "salary")
  

min_messages, max_messages = MinMaxArray(data_dict, "from_messages")
  