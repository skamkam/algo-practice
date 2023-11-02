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
    #root.left.left.left = BTNode(3)
    print(inOrderWalk(root))
    newroot = fixTree(root)
    newroot.printNode()   # sorts and reorganizes tree
    print(inOrderWalk(newroot))

    print()
    unbalanced = getUnbalancedTree()
    print(isBalanced(unbalanced))

    root = BTNode(1)
    root.left = BTNode(2)
    root.left.right = BTNode(3)
    root.right = BTNode(6)
    root.left.right.left = BTNode(3)
    print(isBalanced(root))

    root = BTNode(3)
    root.left = BTNode(2)
    root.right = BTNode(5)
    root.right.left = BTNode(4)
    print(minDepth(root))
    print(maxDepth(root))


if __name__ == "__main__":
    main()