# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:      
    ret=None
    def lowestCommonAncestor(self, poo: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        start =poo
        def helper(root):
            if (root==None or self.ret!=None): return False
            one = helper(root.left)
            two = helper(root.right)
            med=False
            if (root.val==p.val or root.val==q.val): med= True
            
            if one + two+med >1:
                self.ret=root
            
            return one or two or med
            
        helper(poo)
        return self.ret