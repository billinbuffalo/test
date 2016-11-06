import csv
import numpy as np
import matplotlib.pyplot as plt

myFile = open('/Users/bill/School/MSIT/Data/Long_Term_Occupational_Projections.csv')

reader = csv.reader(myFile)

myList = []

for row in reader:
    myList.append(row)

myFile.close()

print(myList)