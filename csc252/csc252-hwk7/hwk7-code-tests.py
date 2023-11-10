# Name: Sarah Kam
# Peers: N/A
# References: Class notes on Dijkstra's algorithm

def get_initial_parents(graph:dict, initial:str) -> dict:
    parents = {}
    for node in graph.keys():
        if node != None and node != initial:
            parents[node] = None
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key in initial_neighbors.keys():
        parents[key] = initial
    return parents
    
def get_initial_costs(graph:dict, initial:str) -> dict:
    costs = {}
    for node in graph.keys():
        if node != None:
            costs[node] = float("inf")
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key, value in initial_neighbors.items():
        costs[key] = value
    return costs

def find_lowest_cost_node(costs:dict, processed:list) -> str:
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def run_dijkstra(graph:dict, start:str, finish:str) -> list:
    processed = []
    parents = get_initial_parents(graph, start)
    costs = get_initial_costs(graph, start)
    node = find_lowest_cost_node(costs,processed)

    while node is not None:        
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost 
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)

    path = [finish] 
    node = finish
    while (node != start):
        if parents[node] != None:
            node = parents[node]
            path = [node] + path
    return path

def getCost(graph: dict, path:list) -> None:
    """
    Given a path, calculates the time needed to walk that path, then prints it
    as a nicely formatted string with minutes:seconds notation
    Assumes the path is a valid path

    :param graph: (dict) The graph that the path is in, contains the costs
    :param path: (list) The list of nodes that must be traveled for the path

    >>> graph = {'a': {'b': 2}}
    >>> getCost(graph, [a, b])
    2
    """
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[ path[i] ][ path[i+1] ]
    # format the cost into minutes:seconds formatting
    min = str(cost // 60)
    sec = str(cost % 60) if cost%60>=10 else "0" + str(cost%60)
    print ("The time this path takes to walk is " + min + ":" + sec + " minutes")

def getMap() -> dict:
    """
    Returns graph with nodes, edges, and costs, based on walking times with a dog
    on Smith College campus
    Costs are encoded as seconds needed to walk an edge

    :return : (dict) A graph with the nodes, edges, and costs of walking around campus with a dog
    """
    map = {}
    map["Hillyer"] = {"Seelye": 61, "Washburn-Seelye intersection": 105}
    map["Seelye"] = {"Hillyer": 61, "Washburn-Seelye intersection": 28}
    map["Washburn-Seelye intersection"] = {"Hillyer": 105, "Seelye": 28, "Neilson E": 35, "Neilson S": 38, "Washburn-Alumnae intersection": 69}
    map["Neilson E"] = {"Washburn-Seelye intersection": 35, "Neilson S": 49}
    map["Neilson S"] = {"Neilson E": 49, "Washburn-Seelye intersection": 38, "Washburn-Alumnae intersection": 25, "Alumnae": 25}
    map["Washburn-Alumnae intersection"] = {"Neilson S": 25, "Washburn-Seelye intersection": 69, "Alumnae S": 34}
    map["Alumnae"] = {"Neilson S": 25, "Neilson W": 39, "Alumnae S": 80}
    map["Neilson W"] = {"Alumnae": 39}
    map["Alumnae S"] = {"Washburn-Alumnae intersection": 34, "Alumnae": 80, "Ford E": 70}
    map["Ford E"] = {"Alumnae S": 70, "Ford W": 26}
    map["Ford W"] = {"Ford E": 26, "Mendenhall": 65, "Sage": 198}
    map["Mendenhall"] = {"Ford W": 65, "Morris W": 47, "Sage": 47}
    map["Morris W"] = {"Mendenhall": 47, "Morris N": 27}
    map["Morris N"] = {"Morris W": 27, "Sage": 149}
    map["Sage"] = {"Morris N": 149, "Mendenhall": 47, "Ford W": 198}
    return map

def testing() -> None:
    """
    Code for testing various paths between nodes and the costs of those paths
    """
    map = getMap()
    hillyer_fordE_path = run_dijkstra(map, "Hillyer", "Ford E")
    print("\nThe shortest path between Hillyer and Ford's east entrance is", hillyer_fordE_path)
    getCost(map, hillyer_fordE_path)

    fordE_sage_path = run_dijkstra(map, "Ford E", "Sage")
    print("\nThe shortest path between Ford's east entrance and Sage Hall is", fordE_sage_path)
    getCost(map, fordE_sage_path)

    neilsonW_fordE_path = run_dijkstra(map, "Neilson W", "Ford E")
    print("\nThe shortest path between Neilson's west entrance and Ford's east entrance is", neilsonW_fordE_path)
    getCost(map, neilsonW_fordE_path)

    morrisN_sage_path = run_dijkstra(map, "Morris N", "Sage")
    print("\nThe shortest path between Morris' north entrance and Sage Hall is", morrisN_sage_path)
    getCost(map, morrisN_sage_path)

    hillyer_neilsonE_path = run_dijkstra(map, "Hillyer", "Neilson E")
    print("\nThe shortest path between Hillyer and Neilson's east entrance is", hillyer_neilsonE_path)
    getCost(map, hillyer_neilsonE_path)

def main():
    """
    Code allowing the user to input start and end points in terminal to query the shortest
    path between them, and outputs the shortest path and cost of that path
    """
    map = getMap()
    locations = map.keys()
    print("\nList of destinations:\n{}".format(locations))
    print("\nWhere would you like to find a path between?")
    start = input("Choose your start location: ")
    while start not in locations:       # protect against bad input
        start = input("Not a valid start location; choose again: ")
    dest = input("Choose your destination: ")
    while dest not in locations:
        dest = input("Not a valid destination; choose again: ")
    path = run_dijkstra(map, start, dest)
    print("The shortest path is:", path)
    getCost(map, path)

#testing()
main()