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

# BUTTA TUTTO SU GITHUB
# db_ratings = pd.read_csv("ratings.csv", sep=',')
# print(db_ratings)

with open('ratings.csv') as f:
    lines = [line.rstrip() for line in f]

print(lines[0:50])

