import warnings
import pandas as pd


warnings.filterwarnings("ignore")

"""
    ASSIGNMENT 3

    Implementing a collaborative recommender

    Implement a user‐based nearest neighbor recommendation algorithm. Write a program that:
    A) Accepts a user ID as an input (on the console)
    B) Then shows the titles and genres of up to 15 movies that this user has rated
        (You can use pandas.merge to merge tables.)
    C) Then displays the 10 movies with the highest predicted relevance score
        according to the nearest neighbor technique.
        (You can use pandas.DataFrame.sample to test your code (because of computation time).)


    Use the MovieLens1M dataset (https://www.kaggle.com/odedgolden/movielens-1m-dataset) 
    for testing your program. Structure your program code in functions
    and/or classes. Implement appropriate error handling procedures. 
    Do not use any library for neither implementing the nearest‐neighbor method nor measuring user similarity.
    Check the recommendations for plausibility by inspecting the recommendations.
    Run experiments with different neighborhood sizes and look at the effects of changing this
    parameter.

"""

"""
    READING DATASETS AND PRINT ONLY THE COLUMNS THAT YOU NEED
"""


# REFACTOR THE CODE TO HAVE JUST A FUNCTION THAT DO ALL THE OPENING WORK AND TAKES COLUMNS FOR ALL THREE DATASET

#############################
def openFile(file, col_names):
    df = pd.read_csv(file,
                     sep='::',
                     engine='python',
                     names=col_names)

    return df


#############################

# MOVIES

movies_df = openFile('dat_archive\\movies.dat',
                     ["MovieID", "Title", "Genres"])

# RATINGS
ratings_df = openFile('dat_archive\\ratings.dat',
                      ["UserID", "MovieID", "Rating", 'Timestamp'])

# USERS
users_df = openFile('dat_archive\\users.dat',
                    ["UserID", "Gender", "Age", "Occupation", "Zip-code"])

####################################################################à

# data_merged_samples = data_merged.sample(frac=0.1, random_state=1)


movies_df['Genres'] = movies_df['Genres'].str.replace('|',',')
movies_df['Genres'] = movies_df['Genres'].str.split(',')

genreList = []

for index, row in movies_df.iterrows():
    genres = row["Genres"]

    for genre in genres:
        if genre not in genreList:
            genreList.append(genre)

# print(genreList[:]) #now we have a list with unique genres

# We need to classify the movies according to their genres.
# Let’s create a new column in the dataframe that will hold the binary
# values whether a genre is present or not in it.

def binary(genre_list):
    binaryList = []

    for genre in genreList:
        if genre in genre_list:
            binaryList.append(1)
        else:
            binaryList.append(0)
    return binaryList

# print("Genre list of 10 elem: ", data_merged_samples['Genres'][:100])
movies_df['genres_bin'] = movies_df['Genres'].apply(lambda x: binary(x))
# pd.set_option("display.max_rows", None, "display.max_columns", None)
###########################################################################
# MERGING DATASET
data_merged = pd.merge(pd.merge(ratings_df, users_df), movies_df) # pd.merge(left, right)

# CONVERT RATING TO FLOAT NUMBER
data_merged['Rating'] = data_merged['Rating'].astype('float')

###########################################################################
# A) Accepts a user ID as an input (on the console)

# REQUEST FOR USERID. HANDLE EXCEPTION
try:
    input_user_ID = int(input("Enter User ID: "))
except ValueError:
    print("That was no valid number. Insert a valid number.")

# DISPLAY THE ENTIRE DATASET
pd.set_option("display.max_rows", None, "display.max_columns", None)


# B) Then shows the titles and genres of up to 15 movies that this user has rated
#    (You can use pandas.merge to merge tables.)

# LOOK FOR THE MATCH BETWEEN THE INPUT USER AND THE ID INSIDE THE DATAFRAME
try:
    requested_user = data_merged[data_merged['UserID'] == input_user_ID][['Title', 'Genres', 'Rating', 'UserID']][:15]
except ValueError:
    print(f"The UserID {input_user_ID} doesn't exist! Try again.")

print(requested_user)


# ###########################################################################
"""
    C) Then displays the 10 movies with the highest predicted relevance score
        according to the nearest neighbor technique.
        (You can use pandas.DataFrame.sample to test your code (because of computation time)).
        (You can use pandas.pivot_table to create the User‐Movie table.)
"""
# ###########################################################################