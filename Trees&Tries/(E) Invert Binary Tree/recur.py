# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        start=root
        def recur(root):
            if root==None: return
            temp=root.right
            root.right=root.left
            root.left=temp
            recur(root.right)
            recur(root.left)
        recur(root)
        return start