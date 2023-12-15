array = []

def preorder(node): 
    if node is None: 
        return
    array.append(node)
    preorder(node.left)
    preorder(node.right)
    return