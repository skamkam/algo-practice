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


#Main:
graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1, 'start':2}, 'b': {'a': 5, 'fin': 5}, 'fin': {}}
path = run_dijkstra(graph, 'start', 'fin')
print("The shortest path is", path)
graph2 = {'Book': {'LP': 5, 'Poster': 0}, 'LP': {'Bass': 15, 'Drum':20}, 'Poster': {'Bass':20, 'Drum':35}, 
          'Drum': {'Piano':10}, 'Bass': {'Piano':20}, 'Piano': {}}
#path2 = run_dijkstra(graph2, 'Book', 'Piano')
#print("The shortest path is", path2)

graph3 = {"E": {"A":7}, "A": {"C":12, "D": 60}, "C":{"B":20, "D":32}, "B":{"A":10}, "D":{}}
#path3 = run_dijkstra(graph3, "E", "D")
#print("The shortest path is", path3)

# the graph
# graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2

# graph["a"] = {}
# graph["a"]["fin"] = 1

# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5

# graph["fin"] = {}

# the costs table
# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity

# the parents table
# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None