# https://leetcode.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        val=0
        stack=[root]
        prev=[]
        while(len(stack)>0):
            val=0
            prev=[]
            for s in stack:
                val+=s.val
                if (s.left): 
                    prev.append(s.left)
                if (s.right):
                    prev.append(s.right)
            stack=prev
            
        return val