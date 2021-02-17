# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.lst=float('-inf')
        def recur(root):
            if root==None:
                return 0
            val1 = recur(root.left)
            val2 = recur(root.right)
            
            temp = max(root.val, root.val+val1,root.val+val2)
            retval=max(val1+val2+root.val, temp)
            self.lst=max(self.lst,retval)
            
            return temp
                
        
        recur(root)
        return self.lst