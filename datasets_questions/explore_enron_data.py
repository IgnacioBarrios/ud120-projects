#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# 13 - Size of the Enron Dataset 146
print "Size of the Enron Dataset:", len(enron_data)
person_total = len(enron_data)
# 14 - For each person, how many features are available? 18
print "Features per person:", len(enron_data["SKILLING JEFFREY K"])

# 15 - How many POIs are there in the E+F dataset?
i=0
for person_name in enron_data:
    if enron_data[person_name]["poi"]:
        i = i + 1
print "POIs in the dataset:", i 
person_POI = i

# 16 Total POIs: 35 (from ) 

# 18 What is the total value of the stock belonging to James Prentice? 1095040
print "Total value stock:", enron_data["PRENTICE JAMES"]["total_stock_value"]

#19 How many email messages do we have from Wesley Colwell to persons of interest? 11
print "Emails from Wesley Colwell to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# 20: What’s the value of stock options exercised by Jeffrey K Skilling? 19250000
print "value of stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# 25 Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature) --> LAY KENNETH L : 103559793
person_list = ["LAY KENNETH L","SKILLING JEFFREY K","FASTOW ANDREW S"]

for person_name in person_list:
    print "Total payments of", person_name, ":" , enron_data[person_name]["total_payments"] 
    
# 27a How many folks in this dataset have a quantified salary? 95
i=0
for person_name in enron_data:
    salary = enron_data[person_name]["salary"]
    print person_name, salary
    if isinstance(salary, int):
        i = i + 1
        
print "Persons with salary:", i 

person_salary = i
# 27b What about a known email address? 111
i=0
for person_name in enron_data:
    email = enron_data[person_name]["email_address"]
    print person_name, email
    if email != "NaN":
        i = i + 1
        
print "Persons with email:", i 


# 29 How many people in the E+F dataset (as it currently exists) 
# have “NaN” for their total payments?  What percentage of people 
# in the dataset as a whole is this?21 out of 146 (about 14%)
i=0
for person_name in enron_data:
    total_payments = enron_data[person_name]["total_payments"]
    print person_name, total_payments
    if total_payments == "NaN":
        i = i + 1

person_no_payment = i
percentage =  i * 100 / person_total
        
print "Persons with no total_payments:", i, "of", person_total , percentage,"(%)"



# 30 How many POIs in the E+F dataset have “NaN” for their total payments?
# What percentage of POI’s as a whole is this? 0 out of 18, or 0%
i=0
for person_name in enron_data:
    total_payments = enron_data[person_name]["total_payments"]
    if total_payments == "NaN" and enron_data[person_name]["poi"]:
        print person_name, total_payments
        i = i + 1

percentage =  i * 100 / person_total
        
print "Persons with no total_payments and POI:", i, "of", person_POI , percentage,"(%)"     

# 32 10 new POIs with NaN in total payments
# What is the new number of people of the dataset? What is the new number of 
#  folks with “NaN” for total payments?
# Now there are 156 folks in dataset, 31 of whom have "NaN" total_payments. 
# This makes for 20% of them with a "NaN" overall

print "person_total = ",  person_total + 10
print "person_no_payment = " , person_no_payment +10 

# 33 What is the new number of POI’s in the dataset? What is the new number 
# of POI’s with NaN for total_payments?
# Now there are 28 POI's, 10 of whom have "NaN" for total_payments
# That's 36% of the POI's who have "NaN" for total_payments
print "person_POI = ",  person_POI + 10

