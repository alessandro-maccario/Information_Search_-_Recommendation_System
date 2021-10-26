import numpy
import statistics
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

# Create a nested list as follows:
#       data = [['Toy Story',21.946943],
#               ['Jumanji',17.015539],
#               ['Grumpier Old Men',11.7129]]
data = [['Toy Story', 21.946943],
        ['Jumanji',17.015539],
        ['Grumpier Old Men', 11.7129]]

# print(data)

# Create a DataFrame object from the nested list with column headings ‘title’ and ‘popularity’.
df_data = pd.DataFrame(data, columns = ['title', 'popularity'])
# print(df_data)

# Create a new DataFrame which has the entries sorted by popularity in ascending order.
df_data_sorted = df_data.sort_values(by=['popularity'])
# print(df_data_sorted)

# Print the popularity values.
# print(df_data_sorted['popularity'])


"""
        Task 3) Analyzing a movie dataset 
        
        Download the movie metadata dataset at  
        https://www.kaggle.com/rounakbanik/the‐movies‐dataset/ 
        (If the link does not work, go to https://www.kaggle.com/rounakbanik and navigate to the 
        Movies Dataset) 
        Write a program that does the following: 
                Read the CSV file “movies_metadata” into a Pandas DataFrame.
                Use the type function to inspect the DataFrame, i.e, inspect the output of the 
                command: 
                        print(type(df))
                Print the information about the first and the last movie in the dataset.
                Show the information about the movie “Jumanji”.
        
        Create a smaller DataFrame called small_df from the given one by considering only the 
        following columns: 'title', 'release_date', 'popularity', 'revenue', 
        'runtime' and 'genres',
        
        Create a function “to_float” to convert the type of its input to float with following code: 
        
        def to_float(x): 
                try: 
                        x = float(x) 
                except: 
                        x = numpy.nan 
                return x   

        Next, add the following code to your program that adds a column names ‘release_year’ 
        to the DataFrame. Inspect how the lambda function is working.
        
        small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy() 
        small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce') 
        small_df['release_year'] = small_df['release_date'].apply
                (lambda x: str(x).split('-')[0] if x != numpy.nan else numpy.nan) 
        small_df['release_year'] = small_df['release_year'].apply(to_float) 
        small_df['release_year'] = small_df['release_year'].astype('float') 
        small_df = small_df.drop(columns="release_date")
        
        Now, print the titles of all movies that were released after the year 2010. 
        
"""

# Write a program that does the following:
#       Read the CSV file “movies_metadata” into a Pandas DataFrame.
#       Use the type function to inspect the DataFrame, i.e, inspect the output of the command:
#               print(type(df))
#               Print the information about the first and the last movie in the dataset.
#               Show the information about the movie “Jumanji”.

movie_df = pd.read_csv('archive/movies_metadata.csv', low_memory=False)
# print(type(df))
# print(type(movie_df))

# Print the information about the first and the last movie in the dataset.
# print(movie_df.iloc[0])
# print(movie_df.iloc[-1])

# Check if the last element is the one gave from the last line of code
# print(movie_df.tail()['title'])

# Show the information about the movie “Jumanji”.
# Do not trunc the row by setting 'display.width'
pd.set_option('display.width', None)
jumanji = movie_df[movie_df['original_title'] == 'Jumanji']
# print(jumanji)

"""
        Create a smaller DataFrame called small_df from the given one by considering only the 
        following columns: 'title', 'release_date', 'popularity', 'revenue', 
        'runtime' and 'genres',
"""

small_df = movie_df.copy()[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']]
# print(small_df)

"""
        Create a function “to_float” to convert the type of its input to float with following code: 
        
        def to_float(x): 
                try: 
                        x = float(x) 
                except: 
                        x = numpy.nan 
                return x   
"""

def to_float(x):
        try:
                x = float(x)
        except:
                x = np.nan

        return x

"""
        Next, add the following code to your program that adds a column names ‘release_year’ 
        to the DataFrame. Inspect how the lambda function is working.
        
        small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy() 
        small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce') 
        small_df['release_year'] = small_df['release_date'].apply
                (lambda x: str(x).split('-')[0] if x != numpy.nan else numpy.nan) 
        small_df['release_year'] = small_df['release_year'].apply(to_float) 
        small_df['release_year'] = small_df['release_year'].astype('float') 
        small_df = small_df.drop(columns="release_date")
        
        Now, print the titles of all movies that were released after the year 2010. 
"""

small_df = movie_df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce')
small_df['release_year'] = small_df['release_date'].apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
small_df['release_year'] = small_df['release_year'].apply(to_float)
small_df['release_year'] = small_df['release_year'].astype('float')
small_df = small_df.drop(columns='release_date')

# Now, print the titles of all movies that were released after the year 2010.
# print(small_df[small_df['release_year'] > 2010.0])

"""
        Task 4) Analyzing a rating dataset
         
        - Read the file “ratings_small.csv” into a Pandas DataFrame. 
        - Our goal is now to compute for every movie its mean and median rating value. For each 
          movie, we would therefore like to print a dictionary like this:  
          {'id': 1, 'rating_mean': 3.8724696356275303, 'rating_median': 4.0} 
                        - Use the method “groupBy” to organize the DataFrame by “movieID”.                        
                        - Iterate over the resulting grouped data structure 
                                - For each tuple, use the methods “mean()” and “median()” to determine 
                                the values for each movie.
                                - Add a new dictionary entry to the resulting list. 
                        - Print the list of dictionaries.
"""

ratings_small = pd.read_csv('archive/ratings_small.csv')
# print(type(ratings_small))
print(ratings_small.columns.values)

grouped_rating_small = ratings_small.groupby(by=['movieId'])
# print(grouped_rating_small.head())

# - Iterate over the resulting grouped data structure:
#       - For each tuple, use the methods “mean()” and “median()” to determine the values for each movie.
#       - Add a new dictionary entry to the resulting list
# - Print the list of dictionaries.

# mean_rating = [{'id': grouped_rating_small.get_group(key)['movieId'].unique()[0],
#                'rating_mean': grouped_rating_small.get_group(key)['rating'].mean(),
#                'rating_median': grouped_rating_small.get_group(key)['rating'].median()}
#                for key, item in grouped_rating_small]

# print(mean_rating)


"""
        Task 5) Finding similar users 
                - Read the file “ratings_small.csv” into a Pandas DataFrame. 
                - Determine the set of users watched by an arbitrary user A (e.g. the first one) 
                        - Group the DataFrame by “userID” (using the groupBy‐function)
                        - Take the first group/user (using “get_group”), access the rated movies by ID and 
                        use the “set” function to create a set of the returned values. 
                        - Print the set of rated movies for user A.
                - Given this set of movies, our goal is now to find other users who have rated at least three 
                of the movies that user A has rated. Proceed as follows.
                        - Iterate over the already grouped DataFrame
                                - Access the rated movies
                                - Use a set intersection operation to see if the current user has rated at 
                                least three of the movies that user A has rated.
                                - If so, remember the user.
                        - Print all users with an intersection of at least three movies.
                                   
"""

# Read the file “ratings_small.csv” into a Pandas DataFrame.
ratings_small = pd.read_csv('archive/ratings_small.csv')

# Group the DataFrame by “userID” (using the groupBy‐function)
user_watched = ratings_small.groupby(by=['userId'])
# print(user_watched.head())

# Take the first group/user (using “get_group”), access the rated movies by ID and
# use the “set” function to create a set of the returned values.
# Print the set of rated movies for user A.
# TODO:
## Is it user A or user 1? Because we don't have letters but only numbers as userId!
# print(set(user_watched.get_group(1)['movieId']))
user_A_watched_movie_list = set(user_watched.get_group(1)['movieId'])
print(user_A_watched_movie_list)
# Given this set of movies, our goal is now to find other users who have rated at least three
# of the movies that user A has rated. Proceed as follows.
# - Iterate over the already grouped DataFrame
#       - Access the rated movies
#       - Use a set intersection operation to see if the current user has rated at
#         least three of the movies that user A has rated.
#       - If so, remember the user.
# - Print all users with an intersection of at least three movies.

# create a list to store all the users that as the same rating movies than user A/1
same_rating = []

# print([{'id': user_watched.get_group(key)['movieId'].unique()[0],}
#                for key, item in user_watched])

# CREATE THE SECOND LIST OF USER B
user_D_watched_movie_list = set(user_watched.get_group(4)['movieId'])
print(user_D_watched_movie_list)

print(user_A_watched_movie_list.isdisjoint(user_D_watched_movie_list))

# CHECK IF THE TWO SET HAVE AT LEAST THREE ELEMENTS IN COMMON
# FIRST: SORT
# SECOND: COMPARE

sort_A = (sorted(user_A_watched_movie_list))
sort_D = (sorted(user_D_watched_movie_list))

list_of_equal = []
for elem in sort_A:
        for el in sort_D:
                if elem == el:
                        list_of_equal.append(elem)
if len(list_of_equal) >= 3:
        print(list_of_equal)

