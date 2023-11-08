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
        if node != None and node != initial:
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

def getMap():
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

def main():
    map = getMap()
    for k, v in map.items():
        print("\n\nkey: {}\nval: {}".format(k, v))
    path = run_dijkstra(map, "Hillyer", "Ford E")
    print("The shortest path is", path)

main()