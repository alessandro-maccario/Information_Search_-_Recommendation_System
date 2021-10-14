import pandas as pd
from pathlib import Path
from collections import Counter


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


"""
    EXERCISE 2 - Information Search and Recommendation System Course
    Task 2.2) --> Functions and error handling 

    All calculations from the previous Task should now be done within a function called “computeMeanRating”, 
    which takes a file name as an input and returns a float as a result. 
    Define this function, implement appropriate error handling procedures (including exception handling 
    in case the file cannot be read or found), and write a main function that invokes the method.
"""

p = Path('ratings.csv')


def computeMeanRating(file):

    # HANDLING EXCEPTION
    if file.exists():
        # OPEN FILE
        with file.open('r') as f:
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
# print(main(p))

"""
    EXERCISE 3 - Information Search and Recommendation System Course 

    Task 2.3) Functions and return values 

    Extend the function from the previous Task so that it returns not only the mean value, 
    but also the mode and the median. Write a corresponding test method. 
"""


# STATISTIC CLASS
class statisticsRating:

    def openFile(self, file):

        # HANDLING EXCEPTION. OPEN FILE IF EXISTS
        if file.exists():

            with file.open('r') as f:
                # OPEN THE FILE “RATINGS.CSV” AND READ THE CONTENTS LINE BY LINE.
                # f = open(file, 'r')
                lines = f.readlines()
                # STORE EACH RATING IN THE LIST. (List Comprehension)
                result = [x.split(',')[2] for x in lines]

                # CLOSE THE FILE
                f.close()
        else:
            print("Either the file is missing or not readable!")
            exit()

        return result


    def computeMeanRating(self, inputList):

        # CALCULATE THE MEAN
        summa = 0
        # CREATE A NEW LIST WITH THE FIRST ELEMENT AS A NAME COLUMN
        # AND ALL THE VALUES AS IN FLOATING NUMBERS
        new_list = [inputList[0]] + [float(i) for i in inputList[1:]]

        # INITIALISE A COUNT VARIABLE USEFUL TO COUNT HOW MANY NUMBER THERE ARE
        count = 0
        for x in new_list[1:]:
            summa += x
            count += 1

        average_rating = float(round(summa / count))
        return average_rating


    def computeMedianRating(self, input_list):
        lenght = len(input_list)
        middle = int(lenght / 2)
        if lenght % 2:
            return sorted(input_list)[middle]
        else:
            return (sorted(input_list)[middle - 1] + (sorted(input_list)[middle])) / 2


    def computeModeRating(self, input_list):

        c = Counter(input_list)

        for k,v in c.items():
            if v == c.most_common(1)[0][1]:
                return k

        # WITH LIST COMPREHENSION
        # return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


# TEST CLASS AND FUNCTION
# p = Path('ratings.csv')
# m_odd = [1, 2, 3, 4, 5]
# m_even = [1, 2, 3, 4, 5, 6]
# l = [1, 2, 3, 4, 5, 6, 5, 7 ,5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 8, 8, 8, 8]

# INITIALISE THE INSTANCE
# stat_1 = statisticsRating()
# print(stat_1.computeMeanRating(stat_1.openFile(p)))
# print(stat_1.computeMedianRating(m_odd))
# print(stat_1.computeMedianRating(m_even))
# print(stat_1.computeModeRating(l))


"""
    Task 2.4) More data structures and file handling 

    Our next goal is to analyze the genres that are appearing in the file “movies.csv”. 
    Write a procedure that takes the file name as a parameter and prints the following on the screen: 
    
    - All distinct genre names that appear in the file. You can use the Python csv module. 
    - For each genre, determine to how many movies it was assigned. 
    Use a dictionary (genre ‐> counter) to save the number of genre assignments.  
            - Print the number of movies per genre 
            - Determine and print out the most popular genre. 
    - Optional: Sort the genres by the number of movies they are assigned to in descending order. 
    Use a suitable library function.
"""


# READ THE DATABASE
movies_db = pd.read_csv('movies.csv', sep=',')

def splitElementInColumn(db, column):
    # SPLIT THE ELEMENTS IN COLUMN
    b = db[column].apply(lambda row: row.split("|"))

    # LOOP THROUGH EVERY ROW OF B AND ADD EACH ELEMENT TO A LIST WITH LIST COMPREHENSION
    genres_list = [single_elem for row in b for single_elem in row]

    # CHOOSE THE UNIQUE ELEMENT
    unique_genres = pd.unique(genres_list)

    return unique_genres

# SPLIT THE GENRE COLUMN
movies_db['genres'] = movies_db['genres'].str.split("|")

# EXPLODE THE RESULTS: EACH ROW CONTAINS THE SAME FILM UNDER DIFFERENT CATEGORIES
movies_db = movies_db.explode('genres')

#FOR EACH GENRE, DETERMINE TO HOW MANY MOVIES IT WAS ASSIGNED.
# COUNT THE VALUES
count_assigned_genre_movies = movies_db.value_counts(subset=['genres']).reset_index(level=[0])

# RENAME THE COLUMN
count_assigned_genre_movies = count_assigned_genre_movies.rename(columns={0: "values"})

# CREATE THE DICTIONARY
genre_counter = count_assigned_genre_movies.set_index("genres").to_dict()["values"]

# DETERMINE AND PRINT OUT THE MOST POPULAR GENRE.
max_genre = max(genre_counter.items(), key = lambda k : k[1])

# # OPTIONAL: SORT THE GENRES BY THE NUMBER OF MOVIES THEY ARE ASSIGNED TO IN DESCENDING ORDER.
#   USE A SUITABLE LIBRARY FUNCTION. --> DONE ALREADY BEFORE!!!


"""
    Task 2.5) Modules and classes 
    Define a Python module “utilityModule” including a class “Statistics” and add the function defined in 
    Task 2.2 as a method to this class.  
    Write a test program that invokes the method (and thus prints the mean rating in the dataset). 
"""

# LOOK AT UTILITYMODULE.PY FILE