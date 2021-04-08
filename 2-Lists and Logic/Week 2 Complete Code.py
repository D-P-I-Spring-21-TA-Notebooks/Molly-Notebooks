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