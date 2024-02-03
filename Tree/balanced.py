from turtle import right


def isBalanced(root): 
    def dfs(root): 
        if root is None: 
            return [None, 0]
        leftSubTree = dfs(root.left)
        rightSubTree = dfs(root.right)
        balanced = leftSubTree[0] and rightSubTree[0] and abs(leftSubTree[1] - rightSubTree[1]) <= 1
        height = 1 + max(leftSubTree[1], rightSubTree[1])
        return [balanced, height]
    return dfs(root)[0]