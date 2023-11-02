from hwk6Answer import *
from time import time

def getSmallDirectedExample() -> dict:
    graph = {}
    graph["you"] = ["alice", "bob"]
    graph["bob"] = ["peggy"]
    graph["alice"] = ["claire"]
    graph["claire"] = ["tom", "jonny"]
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []
    return graph

def getSmallTree() -> BTNode:
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    return root

def getUnbalancedTree() -> BTNode:
    root = BTNode(10)
    root.left = BTNode(4)
    root.left.left = BTNode(3)
    root.left.right = BTNode(6)
    root.left.left.left = BTNode(5)
    root.left.left.left.right = BTNode(6)    
    root.right = BTNode(3)
    return root

def main():
    starttime = time()
    POL_helper()    #Test is hwk6Answer.py imported correctly.
    dag_graph = getSmallDirectedExample()
    smaller_dag_graph = {"a": [], "b": [], "c": ["b"]}  # contains loner node 'a'
    small_tree = getSmallTree()
    unbalanced_tree = getUnbalancedTree()
    
    ### FROM HERE ON ARE MY OWN TEST CASES
    print("\nTesting convertDAGToUG()...")
    print(dag_graph)
    ug_graph = convertDAGToUG(dag_graph)
    print(ug_graph)     # turned into undirected edges
    print(smaller_dag_graph)
    print(convertDAGToUG(smaller_dag_graph))

    print("\nTesting findBFSPath()...")
    print(findBFSPath(dag_graph, "you", "tom"))     # Path exists
    print(findBFSPath(dag_graph, "tom", "you"))     # Path doesn't exist
    print(findBFSPath(ug_graph, "you", "tom"))      # Path exists
    print(findBFSPath(ug_graph, "tom", "you"))      # Path exists
    print(findBFSPath({}, "A", "B"))                # Path doesn't exist - start/end nodes not in graph
    print(findBFSPath(smaller_dag_graph, "c", "a")) # Path doesn't exist

    print("\nTesting inOrderWalk()...")
    print(inOrderWalk(small_tree))
    print(inOrderWalk(unbalanced_tree))
    print(inOrderWalk(BTNode(5)))

    print("\nTesting listToTree()...")
    # Note: Printing the data at the root
    print("root's data is:", listToTree([0,1,2,3,4,5,6,7,8,9]).data )
    # print("root's data is:", listToTree([]).data )    # Breaks b/c empty list returns None, not BTNode; no .data attribute
    print("root's data is:", listToTree([1]).data )
    print("root's data is:", listToTree([4,4,4,4,5,5,5]).data )     # prints 4
    print("root's data is:", listToTree([9,4,5,7,2,1,3]).data )     # prints 7; function builds any BT off a list

    print("\nTesting fixTree()...")
    # These will print the root node of the fixed BST, approx midpoint of nodes' data
    print("root's data is:", fixTree(small_tree).data )
    print("root's data is:", fixTree(unbalanced_tree).data )
    # listToTree just turns any list into a BT, doesn't automatically sort it
    # I'm gonna use it here to construct a tree that's out of order, then call fixTree() on that
    bin_tree = listToTree([5,67,8,49,55,23,6,8,5,101])
    print("root's data is:", fixTree(bin_tree).data )      # returns 23, the midpt of the vals in list

    print("\nTesting isBalanced()...")
    print(isBalanced(small_tree))   # True
    print(isBalanced(unbalanced_tree))      # False
    print(isBalanced(bin_tree))     # True since listToTree() creates balanced trees

    print("\nTime taken:", str(time() - starttime), "seconds")

if __name__ == "__main__":
    main()