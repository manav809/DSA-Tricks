# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root): 
            if root is None:
                return [True, 0]

            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)
            balanced = leftSubTree[0] and rightSubTree[0] and (abs(leftSubTree[1] - rightSubTree[1]) < 2)
            return [balanced, 1 + max(leftSubTree[1], rightSubTree[1])]

        x = dfs(root)
        return x[0]
    
