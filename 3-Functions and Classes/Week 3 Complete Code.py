#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:40:49 2021

@author: mollybair
"""
import pandas as pd

## Lists and List Attributes ##
numbers = [99, 5, 17, 23, 3]
numbers.append(3)
print(numbers)

numbers.sort()
print(numbers)

count_threes = numbers.count(3)
print(count_threes)

## Create a Class ##
class SeaTurtle:
    # Define class variables
    habitat = 'ocean'
    
    # Define constructor
    def __init__(self, name, age, species):
        # Name, age, and species are instance variables
        self.name = name
        self.age = age
        self.species = species
    
    # Define methods
    def introduce(self):
        print('Hi! My name is ' + self.name + '. I am a ' + self.species + \
              ' and I am ' + str(self.age) + ' years old.')
            
    def to_list(self):
        attributes = [self.name, self.age, self.species, self.habitat]
        return attributes
    
    def compare_species(self, other):
        if (self.species == other.species):
            print(self.name + ' and ' + other.name + ' are the same species.')
        else:
            print(self.name + ' and ' + other.name + ' are not the same species.')
        
    
my_turtle = SeaTurtle('Lucy', 11, 'Loggerhead sea turtle')
my_turtle.introduce()

my_other_turtle = SeaTurtle('Jacob', 18, 'Green sea turtle')
turtle_data = [my_turtle.to_list(), my_other_turtle.to_list()]
my_turtles = pd.DataFrame(turtle_data, columns=['Name', 'Age', 'Species', 'Habitat'])
print(my_turtles)

my_turtle.compare_species(my_other_turtle)