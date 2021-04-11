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
        depth=0
        height=0
        curr=root
        stack=[]
        while(curr or len(stack)>0):
            while(curr):
                stack.append((curr,height))
                height+=1
                curr=curr.left
            
            curr,height=stack.pop()
            if height>depth: 
                depth=height
                val=curr.val
            elif height==depth: val+=curr.val
            
            curr=curr.right
            height+=1

        return val