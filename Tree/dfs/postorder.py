
array = []

def postorder(node):
    if node is None: 
        return
    postorder(node.left)
    postorder(node.right)
    array.append(node)
    return