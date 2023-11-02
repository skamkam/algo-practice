# Name: Sarah Kam
# Peers: N/A
# References: Class notes on quicksort, CLRS section on binary trees

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

    >>> convertDAGToUG( {'a': ['b'], 'b': []} )
    {'a': ['b'], 'b': ['a']}
    >>> convertDAGToUG( {} )
    {}
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
        if ug.get(node) == None:            # if atp node is still not added
            ug[node] = []                   # it has no neighbors, so add node and value []
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
    >>> findBFSPath( {"A": ["B", "C"], "B": [], "C": ["D"], "D": []}, "D", "A" )
    None
    >>> findBFSPath({}, "A", "B")
    None
    >>> findBFSPath( {"A": ["B", "C"], "B": ["A"], "C": ["A"]}, "C", "B")
    ["C", "A", "B"]
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
                    if n not in searched:   # check if we've searched it yet
                        search_queue.append(n)  # add to search_queue
                        parents[n] = cur_node   # add the neighbor with the cur_node as parent
                # Marks this cur_node as searched
                searched.append(cur_node)
    return None

def inOrderWalk(root:BTNode) -> list:
    """
    Traverses a tree in order (L, N, R) and returns the data elements in the tree in a list.

    :param root: (BTNode) The root of the tree to be traversed
    :return : (list) A list of the data elements in the tree, traversed in order
    
    >>> root = BTNode(5)
    >>> root.left = BTNode(2)
    >>> root.right = BTNode(1)
    >>> root.left.left = BTNode(4)
    >>> inOrderWalk(root)
    [4, 2, 5, 1]
    """
    ans = []
    if root.left != None:
        for val in inOrderWalk(root.left):
            ans.append(val)
    ans.append(root.data)
    if root.right != None:
        for val in inOrderWalk(root.right):
            ans.append(val)
    return ans
    
    
def listToTree(tree_as_list:list) -> BTNode:
    """
    Takes an ascending order sorted array and turns the values in the array into
    a binary search tree, returning the root node

    :param tree_as_list: (list) The list containing sorted values to be converted into a BST
    :return : (BTNode) The root node of the BST created from tree_as_list

    >>> listToTree([0,1,3,4,5,7,8,10])
    BTNode(5)
    >>> listToTree([])
    None
    >>> listToTree([0])
    BTNode(0)
    """
    if len(tree_as_list) == 0:
        return None
    # reverse engineer binary search in a sorted array
    m = len(tree_as_list) // 2
    l = m // 2
    r = (len(tree_as_list)+m) // 2
    node = BTNode(tree_as_list[m])
    if l < m:
        node.left = listToTree(tree_as_list[:m])   # node creator on left half
    if r > m:
        node.right = listToTree(tree_as_list[m+1:])    # node creator on right half
    return node

def quicksort(arr:list) -> list:    # helper function for fixTree()
    """
    Performs quicksort on an input array

    :param arr: (list) The input array to be sorted
    :return : (list) The sorted output array

    >>> quicksort([7,3,5,8,6])
    [3,5,6,7,8]
    >>> quicksort([])
    []
    """
    if len(arr) < 2:    # base case
        return arr
    else:               # recursive case  
        pivot = arr[0]      # choose the first elt as pivot
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
def fixTree(root:BTNode) -> BTNode:
    """
    Given a binary tree of integers that are not sorted into a binary search tree,
    sorts the tree into a binary search tree and returns the root node. Uses a helper
    function, quicksort, to sort the unsorted tree's data into a sorted list.

    :param root: (BTNode) The root of the unsorted tree
    :return : (BTNode) The root of the sorted tree

    >>> root = BTNode(5)
    >>> root.left = BTNode(2)
    >>> root.right = BTNode(1)
    >>> root.left.left = BTNode(4)
    >>> fixTree(root)   # original root is 5
    BTNode(4)   # sorts and returns the sorted tree's root, 4
    """
    data = inOrderWalk(root)
    sorteddata = quicksort(data)
    return listToTree(sorteddata)

def maxDepth(node:BTNode) -> int:
    """
    Finds the maximum depth of a rooted tree, aka the length of the longest path to a leaf node

    :param node: (BTNode) The node to check the depth of
    :return : (int) The depth of that branch
    
    >>> root = BTNode(3)
    >>> root.left = BTNode(2)
    >>> root.right = BTNode(5)
    >>> root.right.left = BTNode(4)
    >>> maxDepth(root)
    2   # the two leaf branches are, respectively, 1 deep and 2 deep; returns 2
    """
    if node.left == None and node.right == None:    # the node is a leaf node
        return 0
    else:
        if node.left != None:
            left_depth = 1 + maxDepth(node.left)
        else:
            left_depth = 0
        if node.right != None:
            right_depth = 1 + maxDepth(node.right)
        else:
            right_depth = 0
        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth

def minDepth(node:BTNode) -> int:
    """
    Finds the minimum depth of a rooted tree, aka the length of the shortest path to a leaf node

    :param node: (BTNode) The node to check the depth of
    :return : (int) The depth of that branch
    
    >>> root = BTNode(3)
    >>> root.left = BTNode(2)
    >>> root.right = BTNode(5)
    >>> root.right.left = BTNode(4)
    >>> minDepth(root)
    1   # the two leaf branches are, respectively, 1 deep and 2 deep; returns 1
    """
    if node.left == None and node.right == None:    # the node is a leaf node
        return 0
    else:
        if node.left != None and node.right != None:    # 2 kids
            left_depth = 1 + minDepth(node.left)
            right_depth = 1 + minDepth(node.right)
            if left_depth < right_depth:
                return left_depth
            else:
                return right_depth
        elif node.right != None:    # only a right kid
            return (1 + minDepth(node.right))
        elif node.left != None:     # only a left kid
            return (1 + minDepth(node.left))

def isBalanced(root:BTNode) -> bool:
    """
    Checks if a binary tree is balanced, where a balanced tree is defined to be a tree
    such that no two leaf nodes differ in distance from the root by more than one.    

    :param root: (BTNode) The root of the binary tree we want to check
    :return : (bool) Whether or not the binary tree is balanced

    >>> root = BTNode(1)
    >>> root.left = BTNode(2)
    >>> root.left.right = BTNode(3)
    >>> isBalanced(root)
    True    # the only leaf node is root.left.right, so min and max depth are the same

    >>> root.right = BTNode(6)      # continuing from previous tree
    >>> root.left.right.left = BTNode(3)
    >>> isBalanced(root)
    False   # the two leaf nodes are root.right and root.left.right.left; min=1, max=3
    """
    return (maxDepth(root) - minDepth(root)) <= 1

def printTree(root:BTNode) -> None:
    pass    # BONUS

