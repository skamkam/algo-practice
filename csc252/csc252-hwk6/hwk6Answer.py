from collections import deque

#### DO NOT EDIT - START ####
def POL_helper():
    print("File Imported")

class BTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
#### DO NOT EDIT - END ####

def convertDAGToUG(dag_graph:dict) -> dict:
    """
    Converts a directed acyclic graph into an undirected graph by
    turning each directed edge into an undirected edge.
    
    :param dag_graph: (dict) The directed acyclic graph
    :return : (dict) The converted undirected graph

    >>> convertDAGToUG( {'a': ['b']} )
    {'a': ['b'], 'b': ['a']}
    >>> convertDAGToUG( {} )
    {}
    >>> convertDAGToUG( {'you': ['alice', 'bob'], 'bob': ['peggy'], 'alice': ['claire'],
        'claire': ['tom', 'jonny'], 'peggy': [], 'tom': [], 'jonny': []} )
    {'you': ['alice', 'bob'], 'alice': ['you', 'claire'], 'bob': ['you', 'peggy'], 'peggy': ['bob'], 
    'claire': ['alice', 'tom', 'jonny'], 'tom': ['claire'], 'jonny': ['claire']}
    """
    ug = {}
    for node in dag_graph.keys():
        for neighbor in dag_graph[node]:
            if ug.get(node) == None:        # if that node doesn't exist yet
                ug[node] = [neighbor]       # make a node and put neighbor in its values-list
            elif neighbor not in ug[node]:  # if node exists and the neighbor isn't in, add
                ug[node].append(neighbor)
            if ug.get(neighbor) == None:    # if neighbor node doesn't exist yet
                ug[neighbor] = [node]       # make a neighbor node and put og node in val-list
            elif node not in ug[neighbor]:  # if neighbor exists and og isn't in, add
                ug[neighbor].append(node)
    return ug


def findBFSPath(graph:dict, start_node:str, end_node:str) -> list:
    """
    Returns the shortest path found with BFS as a list of nodes to travel to, or None
    if the path does not exist.

    :param graph: (dict) A graph, undirected or directed, that we are running BFS on
    :param start_node: (str) The start node of our BFS
    :param end_node: (str) The end node/target of our BFS
    :return : (list) The list of nodes to travel to get from start_node to end_node,
        or None if the path does not exist

    >>> findBFSPath( {"A": ["B", "C"], "B": [], "C": ["D"], "D": []}, "A", "D" )
    ["A", "C", "D"]
    >>> findBFSPath({}, "A", "B")
    None
    >>> findBFSPath( {"A": ["B", "C"], "B": [], "C": ["D"], "D": []}, "D", "A" )
    None
    >>> findBFSPath( {"A": ["B", "C"], "B": ["A"], "C": ["A"]}, "A", "C")
    ["A", "C"]
    """
    if graph.get(start_node) == None or graph.get(end_node) == None:
        return None     # if start/end node isn't in the graph, return None

    search_queue = deque()      # create a queue
    search_queue += [start_node]    # start node has to be list type
    # This array is how you keep track of which people you've searched before.
    searched = []
    parents = {}
    while search_queue:
        cur_node = search_queue.popleft()   # deque is "double ended queue"
        # Only search this cur_node if you haven't already searched it
        if cur_node not in searched:
            if cur_node == end_node:
                path = [end_node]
                while cur_node != start_node:
                    cur_node = parents[cur_node]    # update cur_node to its own parent
                    path.insert(0, cur_node)
                return path
            else:
                for n in graph[cur_node]:   # every neighbor
                    search_queue.append(n)  # add to search_queue
                    parents[n] = cur_node   # add the neighbor with the cur_node as parent
                # Marks this cur_node as searched
                searched.append(cur_node)
    return None


def inOrderWalk(root:BTNode) -> list:
    """
    Write the function inOrderWalk(root:BTNode) -> list that walks or traverses
    a tree in order (left, node, right) and returns the data elements in the tree in a list.
    """
    # how to tell if it's the base case?!
    # recursive left, node, right... like DFS
    if root == None:
        return root
    answers = [inOrderWalk(root.left), root, inOrderWalk(root.right)]
    return answers
    
    
    
def listToTree(tree_as_list:list) -> BTNode:
    """
    Given a sorted (increasing order) array, write the function
    listToTree(tree_as_list:list) -> BTNode to create a binary search tree
    with minimal height. Return the head of the tree.
    """
    def node_creator(lst:list) -> BTNode:
        m = len(lst) // 2
        l = m // 2
        r = m + l
        node = BTNode(lst[m])
        if l != m:
            node.left = node_creator(lst[:m])   # node creator on left half
        if r != m:
            node.right = node_creator(lst[m+1:])    # node creator on right half
        print(node.data)
        return node
    
    node_creator(tree_as_list)
    return None

    
def fixTree(root:BTNode) -> BTNode:
    return None 

def isBalanced(root:BTNode) -> bool:    
    return (maxDepth(root) - minDepth(root)) <= 1

def printTree(root:BTNode) -> None:
    pass    # BONUS

