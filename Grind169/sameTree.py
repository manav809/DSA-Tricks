# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None or (p.val != q.val):
            return False
        leftSubTree = self.isSameTree(p.left, q.left)
        rightSubTree = self.isSameTree(p.right, q.right)
        return leftSubTree and rightSubTree