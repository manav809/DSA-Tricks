from operator import le
import re


def levelOrder(root):
    if root is None: 
        return []
    
    queue = [root]
    result = []
    while queue: 
        length = len(queue)
        level = []
        for i in range(length): 
            node = queue.pop()
            level.append(node)
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        result.append(level)
    return result
