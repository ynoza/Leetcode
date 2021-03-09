# Definition for a binary tree node.
# https://leetcode.com/problems/add-one-row-to-tree/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def recur(root,level):
            nonlocal v, d
            if root==None: return
            elif level+1 == d:
                l=TreeNode(v)
                r=TreeNode(v)
                if root.left:
                    l.left=root.left
                root.left=l
                if root.right:
                    r.right=root.right
                root.right=r
            recur(root.left,level+1)
            recur(root.right,level+1)
        if d==1: 
            n=TreeNode(v)
            n.left=root
            return n
        recur(root,1)
        return root