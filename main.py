import numpy as np
import pandas as pd

"""
    INFORMATION SEARCH AND RECOMMENDATION SYSTEM COURSE
    ASSIGNMENT 2
"""


"""

    Task 2) Playing with Pandas
    Task 2.1) Getting used to Series  

        Create a list of strings as follows: 
            data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']
        Create a Pandas Series from the list, then:
            Print the first element
            Print the first two elements
            Print the last two elements
        Create a new series from the list with defined indexes: [‘a’, ’b’, ’c’].
        Print the element at index position ‘b’.
    
"""

# Create a list of strings as follows:
data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']

# Create a Pandas Series from the list
data_series = pd.Series(data)
# print(data_series)

# Print the first element
# print(data_series[0])

# Print the first two elements
# print(data_series[0:2])

# Print the last two elements
# print(data_series.iloc[[-1, -2]])

# Create a new series from the list with defined indexes: [‘a’, ’b’, ’c’].
new_series = pd.Series(data)
new_series.index = ['a', 'b', 'c']
# print(new_series)

# Print the element at index position ‘b’.
# print(new_series.loc['b'])


"""
    Task 2.2) Getting used to DataFrames
    
    Create a nested list as follows: 
        data = [['Toy Story',21.946943], 
                ['Jumanji',17.015539], 
                ['Grumpier Old Men',11.7129]]
                
    Create a DataFrame object from the nested list with column headings ‘title’ and ‘popularity’. 
    Create a new DataFrame which has the entries sorted by popularity in ascending order. 
    Print the popularity values. 

"""

data = [['Toy Story', 21.946943],
        ['Jumanji',17.015539],
        ['Grumpier Old Men', 11.7129]]

print(data)