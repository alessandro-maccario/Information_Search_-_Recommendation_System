"""
    Write a program that determines the mean rating in the dataset in the following way:
        - Create a list of data type “float” to store all ratings in memory.
        - Open the file “ratings.csv” and read the contents line by line. --> DONE
        - Store each rating in the list.
        - Close the file.
        - Iterate through the resulting list, sum up the values and calculate the average at the end.
        - Print the result.
"""


import numpy as np
import pandas as pd

# OPEN THE FILE “RATINGS.CSV” AND READ THE CONTENTS LINE BY LINE.
f = open('ratings.csv', 'r')

lines = f.readlines()
result = list()

for x in lines:
    result.append(x.split(',')[2])
f.close()

print(result)