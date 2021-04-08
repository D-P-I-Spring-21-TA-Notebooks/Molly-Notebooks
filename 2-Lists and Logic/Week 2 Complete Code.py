#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:45:03 2021

@author: mollybair
"""

# Problem 1: Subset a list based on whether or not the list values appear
# in a second list. 
all_predictors = ['region', 'age', 'race', 'sex', 'educ', 'job_type']
not_significant = ['region', 'sex']
significant = []

for predictor in all_predictors:
    if predictor not in not_significant:
        significant.append(predictor)
print(significant)

significant = [p for p in all_predictors if p not in not_significant]
print(significant)

# Problem 2: Take a list of singular strings and convert them to plural strings
fruits = ['apple', 'banana', 'strawberry']
plural_fruits = []
for fruit in fruits:
    if fruit[-1:] == 'y':
        plural = fruit[0:len(fruit)-1] +'ies'
    else:
        plural = fruit + 's'
    plural_fruits.append(plural)
print(plural_fruits)

# Problem 3: In a given list, multiply values by 2 if they are located at an odd index.
my_list = [1, 17, 5, 23, 87, 2]
for index, value in enumerate(my_list):
    if index%2 != 0:
        my_list[index] = value*2
print(my_list)

# Problem 4: Iterate over a list of lists. 
my_data = [['a', 'b'], ['1', '2'], ['C', 'D']]
for values in my_data:
    print(values)
    for value in values:
        print(value)