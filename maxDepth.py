# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# Given a binary tree, find its maximum depth. 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth_(self, root, depth):
        leftDepth = 0
        rightDepth = 0
        if root.left != None:
            leftDepth = self.maxDepth_(root.left, depth+1)
        if root.right != None:
            rightDepth = self.maxDepth_(root.right, depth+1)
        if leftDepth>rightDepth:
            return leftDepth
        else:
            return max(rightDepth, depth)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return self.maxDepth_(root, 1)