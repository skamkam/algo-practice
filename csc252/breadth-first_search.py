from collections import deque

"""
How to modify this code so that it finds the smallest path?
What data structure to use, how to store a partial path?
"""

def test_graphs(option):
    graph = {}
    if option == "names":
        graph["you"] = ["alice", "bob", "claire"]
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny"]
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny"] = []
    elif option == "undirected":
        graph["A"] = ["B", "C"]
        graph["B"] = ["A"]
        graph["C"] = ["A"]
        graph["D"] = []
    elif option == "directed":
        graph["A"] = ["B", "C"]
        graph["B"] = ["C", "D"]
        graph["C"] = ["D"]
        graph["D"] = []
        graph["E"] = ["B"]
    return graph

def path_exists(graph, start_node, end_node):
    search_queue = deque()      # create a queue
    search_queue += [start_node]    # start node has to be list type
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        cur_node = search_queue.popleft()   # deque is "double ended queue"
        # Only search this cur_node if you haven't already searched them.
        if not cur_node in searched:
            if cur_node == end_node:
                return True
            else:
                search_queue += graph[cur_node]
                # Marks this cur_node as searched
                searched.append(cur_node)
    return False

def main():

    graph = test_graphs("directed")    

    for start in graph.keys():
        for end in graph.keys():
            if start == end:
                continue
            if path_exists(graph, start, end):
                print("There is a path from", start, "to", end)
            else:
                print("No path from", start, "to", end)

main()
