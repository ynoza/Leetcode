https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        lst=[]
        def recur(root,level):
            nonlocal lst
            if root==None: return
            if level==len(lst): lst.append([root.val]) 
            else: lst[level].append(root.val)
            recur(root.left,level+1)
            recur(root.right,level+1)            
        recur(root,0)
        return lst