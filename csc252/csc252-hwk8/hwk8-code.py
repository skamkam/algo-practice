# Name: Sarah Kam
# Peers: N/A
# References: https://github.com/geodatasource/country-borders: data for countries and their neighbors
#       This data is according to ISO 3166-1, and some islands that are under other countries' rule
#       are treated as their own country (such as Aruba, which is a constituent country of the Netherlands)
#   Pandas documentation

import pandas as pd
from collections import deque
from random import choice as random_choice
from time import time

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
    Takes in a dictionary of countries and their neighbors and uses up to 5 colors to color
    the countries such that no country and its neighbor have the same color.
    Chooses a random country as a "seed" for neighbors, then networks across all associated
    neighbors in a BFS-like search until there are no more neighbors; then if not all countries
    have colors yet, choose a random un-colored country as a new "seed" and repeats.

    :param neighbors: (dict) A dictionary of countries relating to a list of each of their neighbors
    :return : (dict) A dictionary of countries and the colors they've been assigned, encoded as 0, 1, 2, 3, 4

    >>> map_color_1({"AD": ["FR", "SP"], "FR": [""], "SP": [""]})
    {"AD": 0, "FR": 1, "SP": 2}
    """
    queue = deque()
    colors = {}
    n = len(neighbors)
    while len(colors) < n:
        if len(queue) == 0:
            queue += [random_choice(list(neighbors))]    # returns a random country
        cur_country = queue.popleft()

        taken_colors = set()
        for neighbor in neighbors[cur_country]:
            if neighbor == '':
                pass
            elif neighbor not in colors.keys():    # neighbor hasn't been assigned a color yet
                if neighbor not in queue:     # and neighbor hasn't been queued yet or checked...
                    queue += [neighbor]
            else:
                taken_colors.add(colors[neighbor])
        
        i = 0
        while i in taken_colors:
            i += 1
        colors[cur_country] = i

    return colors

def map_color_2(neighbors:dict) -> dict:
    """
    Takes in a dictionary of countries and their neighbors and uses up to 6 colors to color
    the countries such that no country and its neighbor have the same color.
    Chooses a random country to color, checks its neighbors, colors it the lowest possible
    number that its neighbors aren't colored with, chooses another random country and repeats.

    :param neighbors: (dict) A dictionary of countries relating to a list of each of their neighbors
    :return : (dict) A dictionary of countries and the colors they've been assigned, encoded as 0, 1, 2, 3, 4, 5
    
    >>> map_color_2({"AD": ["FR", "SP"], "FR": [""], "SP": [""]})
    {"AD": 0, "FR": 1, "SP": 2}
    """
    colors = {}
    for cur_country in neighbors:
        taken_colors = []
        for neighbor in neighbors[cur_country]:
            if colors.get(neighbor) != None:
                taken_colors.append(colors[neighbor])
        i = 0
        while i in taken_colors:
            i+=1
        colors[cur_country] = i
    return colors


def colors_to_csv(country_colors:dict, filename:str) -> None:
    """
    Writes the country_colors dictionary to a csv file, readable by R program for visualization
    """
    with open("{}.csv".format(filename), "w") as file:
        file.write("Name,Color\n")
        for k,v in country_colors.items():
            file.write("{},{}\n".format(k,v))

def main():
    start = time()
    data = pd.read_csv("countries.csv", keep_default_na=False)      # read in country borders csv
    neighbors = borders_to_neighbors(data)      # turn country borders to dictionary-encoded graph

    choice = input("Would you like map coloring option 1 or option 2? Type 1 or 2: ")
    if choice == "1":
        colors1 = map_color_1(neighbors)
        colors_to_csv(colors1, "color1")
    elif choice == "2":
        colors2 = map_color_2(neighbors)
        colors_to_csv(colors2, "color2")

    print("Time taken: {} seconds".format(time() - start))

main()