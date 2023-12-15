array = []

def inorder(node): 
    if node is None: 
        return
    inorder(node.left)
    array.append(node)
    inorder(node.right)
    return
