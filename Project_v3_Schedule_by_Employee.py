'''
Created on Dec 14, 2017

@author: sharina

GOAL: Program that allows for GUI to access an employee's individual schedule
'''
import csv

with open('raw_store_schedule.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    
    for row in csv_reader:
        Day, Store, Shift, Employee = row
    
        if Employee == "Trevor": 
            print("{} is scheduled for {} at {}, from {}".format(Employee, Day, Store, Shift))

