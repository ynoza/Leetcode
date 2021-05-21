# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lst=[TreeNode(0)]
        lst[0].right=root
        def recur(root):
            nonlocal lst
            if root==None: return
            temp1=root.left
            temp2=root.right
            lst[-1].right=root
            lst[-1].left=None
            lst.append(root)
            recur(temp1)
            recur(temp2)
            root.left=None
            
            # root.left=None
        recur(root)
        # print(lst)
        return lst[0].right
            
            
            
            