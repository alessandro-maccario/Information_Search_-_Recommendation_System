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

# result = list()
# For loop
# for x in lines:
#     result.append(x.split(',')[2])
# f.close()

# Store each rating in the list. (List Comprehension)
result = [x.split(',')[2] for x in lines]

# Close the file.
f.close()

# Iterate through the resulting list, sum up the values and calculate the average at the end.

def summa_list(l):
    summa = 0
    new_list = [result[0]] + [float(i) for i in l[1:]]
    for x in new_list[1:]:
        summa += x
    average_rating = summa/len(l)
    return average_rating

# Print the result.
print(summa_list(result))

