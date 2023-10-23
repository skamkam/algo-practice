from collections import deque

def getClassFriends():
    friends = {
        "Cameron": ["Molly", "Caroline", "Casey", "Shalom", "Sydney", "Sabrina"],
        "Casey": ["Caroline", "Sabrina", "Karenna", "Cameron", "Jessica"],
        "Yina": ["Evelyn", "Sophia"],
        "Chris W": ["Ashley", "Sophia"],
        "Lilliana": ["Sophia", "Allison"],
        "Sabrina": ["Cameron", "Shalom", "Casey", "Ramsha"],
        "Lesly": ["Ramsha", "Abby", "Shalom", "Michelle", "Ashley", "Sarah"],
        "Jessica": ["Michelle", "Casey", "Caroline"],
        "Ramsha": ["Sabrina", "Evelyn", "Lesly", "Michelle"],
        "Heather": ["Emma", "Xinran"],
        "Sydney": ["Allie G", "Chris D", "Molly", "Emma", "Cameron"],
        "Anna": ["Aline"],
        "Aline": ["Annie", "Anna"],
        "Annie": ["Karenna", "Sophia", "Shalom", "Michelle", "Caroline", "Emma", "Abby", "Molly", "Evelyn", "Xinran", "Aline"],
        "Karenna": ["Cameron", "Casey", "Emma", "Xinran", "Molly", "Annie", "Caroline"],
        "Sophia": ["Yina", "Chris W", "Evelyn", "Lilliana", "Annie"],
        "Shalom": ["Sabrina", "Michelle", "Cameron", "Annie", "Lesly"],
        "Michelle": ["Jessica", "Ramsha", "Shalom", "Lesly", "Annie"],
        "Allie G": ["Sydney", "Chris D", "Sarah", "Emma"],
        "Ashley": ["Miya", "Chris W", "Xinran", "Lesly"],
        "Allison": ["Lilliana", "Sarah"],
        "Sarah": ["Allison", "Allie G", "Lesly"],
        "Chris D": ["Sydney", "Allie G"],
        "Caroline": ["Molly", "Emma", "Cameron", "Annie", "Karenna", "Casey", "Jessica"],
        "Emma": ["Molly", "Xinran", "Heather", "Allie G", "Caroline", "Sydney", "Karenna", "Annie"],
        "Abby": ["Annie", "Evelyn", "Rachel", "Lesly"],
        "Molly": ["Emma", "Caroline", "Cameron", "Sydney", "Karenna", "Annie", "Xinran"],
        "Evelyn": ["Xinran", "Lilliana", "Abby", "Sophia", "Ramsha", "Annie", "Yina"],
        "Xinran": ["Ashley", "Karenna", "Heather", "Molly", "Evelyn", "Caroline", "Emma"],
        "Miya": ["Ashley"],
        "Rachel": ["Lesly", "Abby"]
    }
    return friends

def getSmallUndirectedExample():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["you", "peggy"]
    graph["alice"] = ["you","peggy"]
    graph["claire"] = ["tom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []
    return graph

def getSmallDirectedExample():
    graph = {}
    graph["you"] = ["alice", "bob"]
    graph["bob"] = ["peggy"]
    graph["alice"] = ["claire"]
    graph["claire"] = ["tom", "jonny"]
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []
    return graph

def path_exists_BFS(graph, start_node, end_node):
    search_queue = deque()
    search_queue += [start_node]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        cur_node = search_queue.popleft()   # the first element added
        if not cur_node in searched:        # Check for cycles.
            if cur_node == end_node:
                return True
            else:
                search_queue += graph[cur_node]
                searched.append(cur_node)   # Marks this cur_node as searched
    return False

def path_exists_DFS_DAG(graph, cur_node, end_node): #, checked_nodes = []):
    # checked_nodes.append(cur_node)
    # creating a list of checked_nodes is cheating the recursive aspect of this
    # it just becomes normal traversal
    if cur_node == end_node:
        return True
    print(cur_node)
    neighbors = graph[cur_node]
    for n in neighbors:
        #if n not in checked_nodes:
        if path_exists_DFS_DAG(graph, n, end_node): # , checked_nodes):
            return True
    return False

def checkPath(graph, start, end):
    if path_exists_BFS(graph, start, end):
        print("There is a path from", start, "to", end)
    else:
        print("No path from", start, "to", end)

def checkEveryPath(graph):
    for start in graph.keys():
        for end in graph.keys():
            if start == end:
                continue
            if path_exists_BFS(graph, start, end):
                print("There is a path from", start, "to", end)
            else:
                print("No path from", start, "to", end)

def main():
    small = getSmallDirectedExample()
    small_undirected = getSmallUndirectedExample()
    #checkEveryPath(small)
    students = getClassFriends()
    #checkPath(students, "Anna", "Miya")
    
    # If call DFS_DAG on an undirected graph, recursive depth exceeds limit
    #print(path_exists_DFS_DAG(students, "Anna", "Miya"))
    print(path_exists_DFS_DAG(small, "alice", "claire"))

main()
