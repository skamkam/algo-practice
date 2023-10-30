from hwk6Answer import *

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
    root.left.right = BTNode(50)
    return root

def main():
    POL_helper()    #Test is hwk6Answer.py imported correctly.
    dag_graph = getSmallDirectedExample()
    small_tree = getSmallTree()
    
    ### FROM HERE ON ARE MY OWN TEST CASES
    dag_graph2 = {'a': ['b']}
    dag_graph3 = {}

    ug_1 = convertDAGToUG(dag_graph)
    #print(findBFSPath(ug_1, "peggy", "you"))

    #print(findBFSPath( {"A": ["B", "C"], "B": [], "C": ["D"], "D": []}, "A", "D" ))
    #print(findBFSPath({}, "A", "B"))
    #print (findBFSPath( {"A": ["B", "C"], "B": [], "C": ["D"], "D": []}, "D", "A" ))
    #print(findBFSPath( {"A": ["B", "C"], "B": ["A"], "C": ["A"]}, "A", "C"))

    #print(convertDAGToUG( {'a': ['b'], 'b': []} ))

    print(inOrderWalk(small_tree))
    print()

    lst = [0]
    lst_tree_node = listToTree(lst)
    lst_tree_node.printNode()
    #print(inOrderWalk(lst_tree_node))
    #print(listToTree([]))

    root = BTNode(5)
    root.left = BTNode(2)
    root.right = BTNode(1)
    root.left.left = BTNode(4)
    print(inOrderWalk(root))
    newroot = fixTree(root)
    newroot.printNode()   # sorts and reorganizes tree
    print(inOrderWalk(newroot))


if __name__ == "__main__":
    main()