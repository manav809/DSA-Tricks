# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(root):
        def dfs(root):
            if root is None:
                return 0
            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)
            return 1 + max(leftSubTree,rightSubTree)
        return dfs(root)