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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1