"""
    Task 2.5) Modules and classes
    Define a Python module “utilityModule” including a class “Statistics” and add the function defined in
    Task 2.2 as a method to this class.
    Write a test program that invokes the method (and thus prints the mean rating in the dataset).
"""
from pathlib import Path
from main import computeMeanRating


path_file = Path('ratings.csv')


class Statistics:

    def recallComputeMeanRating(self, path_file):
        self.path_file = path_file
        return computeMeanRating(self.path_file)


# INSTANTIATE THE CLASS:
instance = Statistics()

print("Average's Rating: ", instance.recallComputeMeanRating(path_file))
