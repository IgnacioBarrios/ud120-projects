# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:27:35 2018

@author: CASA
"""

""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    max_value = max(data) / 1.0
    min_value = min(data) / 1.0
    output=[]
    
    for value in arr:
        output.append((value -min_value)/(max_value - min_value))
    
    return output

# tests of your feature scaler--line below is input data
# Hay que poner el , para tener floats    
data = [115., 140., 175.]
print featureScaling(data)


def featureScaling_value(value, min_value,max_value):
    
    output = ((value -min_value)/(max_value - min_value))
    
    return output

from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print rescaled_weight



