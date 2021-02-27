# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        ret=[0]
        def recur(root):
            if root==None: return
            recur(root.right)
            root.val+=ret[0]
            ret[0]=root.val
            recur(root.left)
            return
            
            
        start=root
        recur(root)
        return start