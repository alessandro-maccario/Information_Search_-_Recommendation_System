import pprint
import numpy as np
import pandas as pd


"""
    INFORMATION SEARCH AND RECOMMENDATION SYSTEM COURSE
    ASSIGNMENT 2
"""

"""

    Task 2) Playing with Pandas
    Task 2.1) Getting used to Series  

        - Create a list of strings as follows: 
            data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']
        - Create a Pandas Series from the list, then:
            Print the first element
            Print the first two elements
            Print the last two elements
        - Create a new series from the list with defined indexes: [‘a’, ’b’, ’c’].
        - Print the element at index position ‘b’.
    
"""

# Create a list of strings as follows:
data = ['Toy Story', 'Jumanji', 'Grumpier Old Men']

# Create a Pandas Series from the list
data_series = pd.Series(data)
print("Pandas Series:")
pprint.pprint(data_series, width=1)

# Then print the first element
print("\n First element is: ", data_series[0])

# Print the first two elements
print("\n First two elements are:")
pprint.pprint(data_series[0:2], width=1)

# Print the last two elements
print("\n Last two elements are: ")
pprint.pprint(data_series.iloc[[-1, -2]], width=1)

# Create a new series from the list with defined indexes: [‘a’, ’b’, ’c’].
new_series = pd.Series(data)
new_series.index = ['a', 'b', 'c']
print("\n Create a new series from the list: ")
pprint.pprint(new_series, width=1)

# Print the element at index position ‘b’.
print("\n Element at position 'b' is: ")
pprint.pprint(new_series.loc['b'], width=1)

"""
    Task 2.2) Getting used to DataFrames

    - Create a nested list as follows:
        data = [['Toy Story',21.946943],
                ['Jumanji',17.015539],
                ['Grumpier Old Men',11.7129]]

    - Create a DataFrame object from the nested list with column headings ‘title’ and ‘popularity’.
    - Create a new DataFrame which has the entries sorted by popularity in ascending order.
    - Print the popularity values.

"""

data = [['Toy Story', 21.946943],
        ['Jumanji', 17.015539],
        ['Grumpier Old Men', 11.7129]]

# print("Nested list: ", data)
print("\n Nested list:")
pprint.pprint(data, width=1)

# Create a DataFrame object from the nested list with column headings
# ‘title’ and ‘popularity’.
df_data = pd.DataFrame(data, columns = ['title', 'popularity'])
# print("DataFrame from nested list: ", df_data)
print("\n DataFrame from nested list:")
pprint.pprint(df_data, width=1)

# Create a new DataFrame which has the entries sorted by popularity in ascending order.
df_data_sorted = df_data.sort_values(by=['popularity'])
# print("New dataframe with popularity in ascending order: ", df_data_sorted)
print("\n New dataframe with popularity in ascending order: ")
pprint.pprint(df_data_sorted, width=1)

# Print the popularity values.
# print("Popularity values: ", df_data_sorted['popularity'])
print("\n Popularity values: ")
pprint.pprint(df_data_sorted['popularity'], width=1)

"""
        Task 3) Analyzing a movie dataset

        - Download the movie metadata dataset at https://www.kaggle.com/rounakbanik/the‐movies‐dataset/
        (If the link does not work, go to https://www.kaggle.com/rounakbanik and navigate to the Movies Dataset)
        - Write a program that does the following:
                - Read the CSV file “movies_metadata” into a Pandas DataFrame.
                - Use the type function to inspect the DataFrame, i.e, inspect the output of the
                command:
                        print(type(df))
                - Print the information about the first and the last movie in the dataset.
                - Show the information about the movie “Jumanji”.

        - Create a smaller DataFrame called small_df from the given one by considering only the
        following columns: 'title', 'release_date', 'popularity', 'revenue', 'runtime' and 'genres',

        - Create a function “to_float” to convert the type of its input to float with following code:

        def to_float(x):
                try:
                        x = float(x)
                except:
                        x = numpy.nan
                return x

        - Next, add the following code to your program that adds a column names ‘release_year’
        to the DataFrame. Inspect how the lambda function is working.

        small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
        small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce')
        small_df['release_year'] = small_df['release_date'].apply
                (lambda x: str(x).split('-')[0] if x != numpy.nan else numpy.nan)
        small_df['release_year'] = small_df['release_year'].apply(to_float)
        small_df['release_year'] = small_df['release_year'].astype('float')
        small_df = small_df.drop(columns="release_date")

        - Now, print the titles of all movies that were released after the year 2010.
"""

# Read the CSV file “movies_metadata” into a Pandas DataFrame.
movie_df = pd.read_csv('archive/movies_metadata.csv', low_memory=False)
# print(type(movie_df))
print("\n Read the CSV file called movies_metadata: ")
pprint.pprint(type(movie_df), width=1)

# Print the information about the first and the last movie in the dataset.
print("\n Information first movie in the dataset: ")
pprint.pprint(movie_df.iloc[0], width=1)
print("\n Information last movie in the dataset: ")
pprint.pprint(movie_df.iloc[-1], width=1)

# Check if the last element is the one gave from the last line of code
print("\n Last movie of the dataset: ")
pprint.pprint(movie_df.tail()['title'], width=1)

# Show the information about the movie “Jumanji”.
# (Do not trunc the row by setting 'display.width')
pd.set_option('display.width', None)
jumanji = movie_df[movie_df['original_title'] == 'Jumanji']
print("\n Information about Jumanji: ")
pprint.pprint(jumanji, width=1)

# Create a smaller DataFrame called small_df
small_df = movie_df.copy()[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']]

# Create a function “to_float” to convert the type of its input to float with following code:
def to_float(x):
        try:
                x = float(x)
        except:
                x = np.nan

        return x

small_df = movie_df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce')
small_df['release_year'] = small_df['release_date'].apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
small_df['release_year'] = small_df['release_year'].apply(to_float)
small_df['release_year'] = small_df['release_year'].astype('float')
small_df = small_df.drop(columns='release_date')

# Now, print the titles of all movies that were released after the year 2010.
print("\n Titles released after the year 2010: ")
pprint.pprint(small_df[small_df['release_year'] > 2010.0], width=1)


"""
        Task 4) Analyzing a rating dataset

        - Read the file “ratings_small.csv” into a Pandas DataFrame.
        Our goal is now to compute for every movie its mean and median rating value. For each
        movie, we would therefore like to print a dictionary like this:
        {'id': 1, 'rating_mean': 3.8724696356275303, 'rating_median': 4.0}
                        - Use the method “groupBy” to organize the DataFrame by “movieID”.
                        - Iterate over the resulting grouped data structure
                                - For each tuple, use the methods “mean()” and “median()” to determine
                                the values for each movie.
                                - Add a new dictionary entry to the resulting list.
                        - Print the list of dictionaries.
"""

# Read the file “ratings_small.csv” into a Pandas DataFrame.
ratings_small = pd.read_csv('archive/ratings_small.csv')
print("\n Read the file 'ratings_small.csv' into a Pandas DataFrame: ")
pprint.pprint(ratings_small, width=1)

# Use the method “groupBy” to organize the DataFrame by “movieID”.
grouped_rating_small = ratings_small.groupby(by=['movieId'])
print("\n GroupBy to organize the DataFrame by 'movieId': ")
pprint.pprint(grouped_rating_small.head(), width=1)

# Iterate over the resulting grouped data structure
mean_rating = [{'id': grouped_rating_small.get_group(key)['movieId'].unique()[0],
               'rating_mean': grouped_rating_small.get_group(key)['rating'].mean(),
               'rating_median': grouped_rating_small.get_group(key)['rating'].median()}
               for key, item in grouped_rating_small]

# Print the list of dictionaries.
print("\n Mean rating is: ")
pprint.pprint(mean_rating, width=1)


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
print("\n DataFrame grouped bu userId: ")
pprint.pprint(user_watched.head(), width=1)

# First User A/1
user_A_watched_movie_list = set(user_watched.get_group(1)['movieId'])

# Create a list to store all the users that as the same rating movies than user A/1
same_rating = []

# Check if the two set have at least three elements in common using set opeartion "&"
for i in range(2, len(user_watched['userId'])):
        intersection_users_movie = (user_A_watched_movie_list & set(user_watched.get_group(i)['movieId']))
        if len(intersection_users_movie) >= 3:
                same_rating.append({i: intersection_users_movie})

print("\n User with same rating of user A/1: ")
for element in same_rating:
    pprint.pprint(element, width=1)
