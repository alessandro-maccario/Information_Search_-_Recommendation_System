"""
    EXERCISE 1 - Information Search and Recommendation System Course

    Write a program that determines the mean rating in the dataset in the following way:
        - Create a list of data type “float” to store all ratings in memory.
        - Open the file “ratings.csv” and read the contents line by line.
        - Store each rating in the list.
        - Close the file.
        - Iterate through the resulting list, sum up the values and calculate the average at the end.
        - Print the result.
"""

# OPEN THE FILE “RATINGS.CSV” AND READ THE CONTENTS LINE BY LINE.
f = open('ratings.csv', 'r')

lines = f.readlines()

# Store each rating in the list. (List Comprehension)
result = [x.split(',')[2] for x in lines]

# Close the file.
f.close()

# Iterate through the resulting list, sum up the values and calculate the average at the end.


def summa_list(list_of_rating):
    summa = 0
    new_list = [list_of_rating[0]] + [float(i) for i in list_of_rating[1:]]

    count = 0
    for x in new_list[1:]:
        summa += x
        count += 1

    average_rating = float(round(summa/count))
    return average_rating


# Print the result.
print(summa_list(result))

# END
