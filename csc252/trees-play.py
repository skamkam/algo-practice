
class BTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def TreeDFS(node: BTNode, item: int) -> bool:
    """
    
    """
    if node == None or item == None:    # check "reasonable" inputs
        return False
    elif node.data == item:
        return True
    elif node.data > item:
        return TreeDFS(node.left, item)
    elif node.data < item:
        return TreeDFS(node.right, item)

def TreeInsertElt(node: BTNode, item: int) -> bool:
    """
    Deleting element: looks to the left and moves it up to the old node's spot
        the biggest node on the left sub-tree (NOT the left child)
    Inserting element: Find the spot
    """
    if item == None:        # check reasonable inputs
        return False
    elif node.data == item:
        return False
    elif node.data > item:
        return TreeDFS(node.left, item)
    elif node.data < item:
        return TreeDFS(node.right, item)

def main():
    #Graph: 2,5,7,10,20,25
    root = BTNode(10)
    root.left = BTNode(5)
    root.right = BTNode(20)
    root.left.left = BTNode(2)
    root.left.right = BTNode(7)
    root.right.right = BTNode(25)

    print(TreeDFS(root, 7))
    print(TreeDFS(root, 20))
    print(TreeDFS(root, 8))
    print(TreeDFS(root, 23))
    print(TreeDFS(root, None))
    print(TreeDFS(None, None))


main()
