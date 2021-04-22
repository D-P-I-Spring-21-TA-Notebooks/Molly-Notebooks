#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:12:52 2021

@author: Molly
"""

class Student():
    def __init__(self, name, grad_year):
        self.name = name
        self.grad_year = grad_year
        
    def introduce(self):
        print('This student is named ' + self.name + ' and they will graduate in ' +\
              str(self.grad_year))

class PublicPolicy(Student):
    def add_policy_area(self, policy_area):
        self.policy_area = policy_area
    
    def when_to_graduate(self, current_year):
        years_left = 0
        try:
            years_left = abs(current_year - self.grad_year)
        except TypeError:
            print('Sorry, you did not enter a valid year.')
        return years_left
    
    def add_certificate(self):
        certificates = ['Data Analytics', 'Markets and Regulation', 'Health Policy']
        this_certificate = input('Please enter a certificate: ')
        while this_certificate not in certificates:
            print('Uh oh! That does not look like a valid certificate.')
            this_certificate = input('Try again: ')
        self.certificate = this_certificate
    
class Undergrad(Student):
    def add_major(self, major):
        self.major = major

def main():
    student_a = Student('Lucy', 2031)
    student_a.introduce()
    
    harris_student = PublicPolicy('Molly', 2021)
    harris_student.add_policy_area('Labor Policy')
    print(harris_student.policy_area)
    molly_years_left = harris_student.when_to_graduate('2021')
    print(molly_years_left)
    harris_student.add_certificate()
    
    college_student = Undergrad('Jacob', 2025)
    college_student.add_major('engineering')
    print(college_student.major)

main()