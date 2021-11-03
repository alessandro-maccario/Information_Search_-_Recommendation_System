"""
    ASSIGNMENT 3

    Implementing a collaborative recommender

    Implement a user‐based nearest neighbor recommendation algorithm. Write a program that:
    A) Accepts a user ID as an input (on the console),
    B) Then shows the titles and genres of up to 15 movies that this user has rated1,
    C) Then displays the 10 movies with the highest predicted relevance score2
    according to the nearest neighbor technique.

    Use the MovieLens1M dataset for testing your program. Structure your program code in functions
    and/or classes. Implement appropriate error handling procedures. Do not use any library for neither
    implementing the nearest‐neighbor method nor measuring user similarity.
    Check the recommendations for plausibility by inspecting the recommendations.
    Run experiments with different neighborhood sizes and look at the effects of changing this
    parameter.

"""

input_user_ID = input("Insert User ID")