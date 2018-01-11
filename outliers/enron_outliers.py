#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

# quitar TOTAL del diccionario
data_dict.pop( "TOTAL", 0 )

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# Buscar cual es el outlier: es el TOTAL
for person_name in data_dict:
    salary = data_dict[person_name]["salary"]
    bonus = data_dict[person_name]["bonus"]

    if salary > 1e6 and bonus > 10e6 and salary != "NaN":
        print "Higher outlier"
        print person_name, salary, data_dict[person_name]["bonus"]
        

# Buscar bonus > 5 y salario sobre 1
for person_name in data_dict:
    salary = data_dict[person_name]["salary"]
    bonus = data_dict[person_name]["bonus"]

    if salary > 1e6 and bonus > 5e6 and salary != "NaN":
        print person_name, salary, data_dict[person_name]["bonus"]        