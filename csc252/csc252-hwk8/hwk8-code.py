# Name: Sarah Kam
# Peers: N/A
# References: https://github.com/geodatasource/country-borders: data for countries and their neighbors
#       This data is according to ISO 3166, and some islands that are under other countries' rule
#       are treated as their own country (such as Aruba, which is a constituent country of the Netherlands)
#   Pandas documentation on read_csv, itertuples

import pandas as pd
from collections import deque
from random import choice as random_choice
from time import time

"""
1. Choose one of the following problems from the lecture notes: "Map Coloring", "Classroom Assignments", or "Traveling Salesperson".
2. From your chosen problem, find or create a dataset of at least 50 elements with appropriate information. I strongly suggest you store this information as a .csv file.
3. Read the data from step 2 into a Python program for analysis.
4. Create functions for two different greedy strategies. For example, one strategy for the set-covering problem discussed in class was to "pick the station that covers the most states", but alternatively you could have "pick the state that is covered by the least stations".
5. Create a main for the user to choose which strategy to run and communicate the output in a readable way (either through another .csv file or on the console output).
"""
def borders_to_neighbors(pd_data:pd.DataFrame) -> dict:
    """
    Takes in a dataframe containing countries and each of their neighbors and turns
    it into a dictionary relating one country to all its neighbors

    :param pd_data: (pd.DataFrame) Raw data containing rows of: a country and one of its neighbors
    :return : (dict) A dictionary containing key:val pairs of a country and a list of all its neighbors

    >>> data = 
            country_code    country_name    country_border_code     country_border_name
            AD              Andorra         FR                      France
            AD              Andorra         ES                      Spain
    >>> borders_to_neighbors(data)
    {"AD": ["FR", "ES"]}
    """
    neighbors = {}
    # neighbors = {"AD": ["FR", "ES"]}
    for row in pd_data.itertuples(index=False, name=None):    # returns tuple of each row
        if row[0] not in neighbors.keys():      # creates a list at each country
            neighbors[row[0]] = []
        if not (pd.isnull(row[2])):     # checking for pandas null object if the country has no neighbors
            neighbors[row[0]].append(row[2])    # neighbors["AD"] appends "FR"
    return neighbors
    

def map_color_1(neighbors:dict) -> dict:
    """
    Takes in a dictionary of countries and their neighbors and assigns 1 of 4 colors to all
    of them such that no country and its neighbor have the same color

    :param neighbors: (dict) A dictionary of countries relating to a list of each of their neighbors
    :return : (dict) A dictionary of countries and the colors they've been assigned, encoded as 0, 1, 2, 3

    >>> neighbors = {"AD": ["FR", "ES"], "FR": [], "ES": []} TODO: check what it actually does with this
    {"AD": 0, "FR": 1, "ES": 2}     # alternatively {"AD": 0, "FR": 1, "ES": 1} works too
    """
    queue = deque()
    country_colors = {}
    # check the alphabetically first country in the list?
    while len(neighbors) > 0:
        if len(queue) == 0:
            queue += [random_choice(list(neighbors))]    # returns a random country
        cur_country = queue.popleft()

        poss_colors = [0,1,2,3]
        for neighbor in neighbors[cur_country]:
            print(neighbor)
            if country_colors.get(neighbor) != None and country_colors[neighbor] in poss_colors:    # if neighbor has a color assigned already
                poss_colors.remove( country_colors[neighbor] )     # remove whatever color
                print("poss colors: ", poss_colors)

        try:
            country_colors[cur_country] = poss_colors[0]
        except:
            print("Method failed")
            raise SystemExit
        
        for n in neighbors[cur_country]:        # add cur_country's neighbors to queue
            if n not in country_colors.keys() and n not in queue:
                queue += [n]
        neighbors.pop(cur_country, None)        # remove current country from possible ones to check
    return country_colors

def main():
    start = time()
    # TODO: Fix this so the reading in data freaking works
    #data = pd.read_csv("countries.csv", header=0, delimiter = ",")
    data = pd.read_csv(r"C:\Users\sarah\Documents\CodingStuff\algo-practice\csc252\csc252-hwk8\countries.csv")
    neighbors = borders_to_neighbors(data)
    print(map_color_1(neighbors))
    #print(len(neighbors)) 249 countries according to ISO 3166
    print("Time taken: {} seconds".format(time() - start))

main()