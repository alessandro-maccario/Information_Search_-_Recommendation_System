"""
    EXERCISE 1 - Information Search and Recommendation System Course
    Task --> Opening files3, list data structure, loops

    Write a program that determines the mean rating in the dataset in the following way:
        - Create a list of data type “float” to store all ratings in memory.
        - Open the file “ratings.csv” and read the contents line by line.
        - Store each rating in the list.
        - Close the file.
        - Iterate through the resulting list, sum up the values and calculate the average at the end.
        - Print the result.
"""

# # OPEN THE FILE “RATINGS.CSV” AND READ THE CONTENTS LINE BY LINE.
# f = open('ratings.csv', 'r')
#
# lines = f.readlines()
#
# # Store each rating in the list. (List Comprehension)
# result = [x.split(',')[2] for x in lines]
#
# # Close the file.
# f.close()
#
# # Iterate through the resulting list, sum up the values and calculate the average at the end.
#
#
# def summa_list(list_of_rating):
#     summa = 0
#     new_list = [list_of_rating[0]] + [float(i) for i in list_of_rating[1:]]
#
#     count = 0
#     for x in new_list[1:]:
#         summa += x
#         count += 1
#
#     average_rating = float(round(summa/count))
#     return average_rating
#
#
# # Print the result.
# print(summa_list(result))
#
# # END


"""
    EXERCISE 2 - Information Search and Recommendation System Course
    Task --> Functions and error handling 

    All calculations from the previous Task should now be done within a function called “computeMeanRating”, 
    which takes a file name as an input and returns a float as a result. 
    Define this function, implement appropriate error handling procedures (including exception handling 
    in case the file cannot be read or found), and write a main function that invokes the method.
"""

from pathlib import Path

p = Path('ratings.csv')


def computeMeanRating(file):
    # HANDLING EXCEPTION
    if p.exists():
        # OPEN FILE
        with p.open('r') as f:
            # OPEN THE FILE “RATINGS.CSV” AND READ THE CONTENTS LINE BY LINE.
            # f = open(file, 'r')
            lines = f.readlines()
            # STORE EACH RATING IN THE LIST. (List Comprehension)
            result = [x.split(',')[2] for x in lines]

            # Close the file.
            f.close()
    else:
        print("Either the file is missing or not readable!")
        exit()

    summa = 0
    # CREATE A NEW LIST WITH THE FIRST ELEMENT AS A NAME COLUMN
    # AND ALL THE VALUES AS IN FLOATING NUMBERS
    new_list = [result[0]] + [float(i) for i in result[1:]]

    # INITIALISE A COUNT VARIABLE USEFUL TO COUNT HOW MANY NUMBER THERE ARE
    count = 0
    for x in new_list[1:]:
        summa += x
        count += 1

    average_rating = float(round(summa / count))

    return average_rating


def main(file):
    return computeMeanRating(file)

# PRINT THE RESULT
print(main(p))
