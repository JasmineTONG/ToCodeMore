/** 
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 * Given a binary tree, find its maximum depth. 
 * The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root==null)
            return 0;
        else 
            return maxDepth(root, 1);
    }
    public int maxDepth(TreeNode root, int depth) {
        int leftDepth = 0;
        int rightDepth = 0;
        if (root.left != null)
            leftDepth = maxDepth(root.left, depth+1);
        if (root.right != null)
            rightDepth = maxDepth(root.right, depth+1);
        if (leftDepth > rightDepth)
            return leftDepth;
        else 
            return Math.max(rightDepth, depth);
    }
}