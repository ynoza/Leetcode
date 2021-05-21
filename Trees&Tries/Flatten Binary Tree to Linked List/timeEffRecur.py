# Definition for a binary tree node.
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
        node=TreeNode(0)
        prev=node
        def recur(root):
            nonlocal prev
            if root==None: return
            node=root.right
            prev.right=root
            prev.left=None
            
            prev=root
            # print(prev)
            
            recur(root.left)
            
            root.left=None
            
            recur(node)
            
            
        recur(root)
        
        return node.right
            
            
            