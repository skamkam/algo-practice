# Name: Sarah Kam
# Peers: N/A
# References: https://github.com/geodatasource/country-borders: data for countries and their neighbors
#       This data is according to ISO 3166-1, and some islands that are under other countries' rule
#       are treated as their own country (such as Aruba, which is a constituent country of the Netherlands)
#   Pandas documentation on read_csv, itertuples
#   https://towardsdatascience.com/visualizing-geospatial-data-in-python-e070374fe621 for mapping
#   https://stackoverflow.com/questions/39578611/geopandas-attributeerror-multipolygon-object-has-no-attribute-exterior
#       For fixing multipolygon error when trying to map

import pandas as pd
import geopandas as gpd
import geoplot as gplt
import json
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
    {"AD": ["FR", "SP"]}
    """
    neighbors = {}
    for row in pd_data.itertuples(index=False, name=None):    # returns tuple of each row
        if row[0] not in neighbors.keys():      # creates a list at each country
            neighbors[row[0]] = []
        if not (pd.isnull(row[2])):     # checking for pandas null object if the country has no neighbors
            neighbors[row[0]].append(row[2])
    return neighbors


def map_color_1(neighbors:dict) -> dict:
    """
    Takes in a dictionary of countries and their neighbors and assigns 1 of 4 colors to all
    of them such that no country and its neighbor have the same color

    :param neighbors: (dict) A dictionary of countries relating to a list of each of their neighbors
    :return : (dict) A dictionary of countries and the colors they've been assigned, encoded as 0, 1, 2, 3

    >>> TODO
    """
    queue = deque()
    country_colors = {}
    n = len(neighbors)
    while len(country_colors) < n:
        if len(queue) == 0:
            queue += [random_choice(list(neighbors))]    # returns a random country
        cur_country = queue.popleft()

        taken_colors = set()
        for neighbor in neighbors[cur_country]:
            if neighbor == '':
                pass
            elif neighbor not in country_colors.keys():    # neighbor hasn't been assigned a color yet
                if neighbor not in queue:     # and neighbor hasn't been queued yet or checked...
                    queue += [neighbor]
            else:
                taken_colors.add(country_colors[neighbor])
        
        poss_colors = ["red", "yellow", "green", "lightblue", "purple","lightgrey"]
        for color in taken_colors:
            poss_colors.remove(color)
        country_colors[cur_country] = poss_colors[0]

    return country_colors

def colors_to_csv(country_colors:dict) -> None:
    """
    Writes the country_colors dictionary to a csv file
    """
    with open("colors.csv", "w") as file:
        file.write("Name,Color\n")
        for k,v in country_colors.items():
            file.write("{},{}\n".format(k,v))


def main():
    start = time()
    # TODO: Fix this so the reading in data freaking works
    #data = pd.read_csv("countries.csv", header=0, delimiter = ",")
    data = pd.read_csv(r"C:\Users\sarah\Documents\CodingStuff\algo-practice\csc252\csc252-hwk8\countries.csv", keep_default_na=False)
    neighbors = borders_to_neighbors(data)
    print(neighbors)
    colors = map_color_1(neighbors)
    colors_to_csv(colors)

    print("Time taken: {} seconds".format(time() - start))

main()