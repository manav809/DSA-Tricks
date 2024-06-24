def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.res = 0
    def dfs(root):
        if root is None:
            return 0
        leftSubTree = dfs(root.left)
        rightSubTree = dfs(root.right)
        self.res = max(self.res, leftSubTree + rightSubTree)
        return 1 + max(leftSubTree, rightSubTree)
    dfs(root)
    return self.res