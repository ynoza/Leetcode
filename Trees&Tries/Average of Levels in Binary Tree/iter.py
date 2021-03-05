# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        lst=[]
        curr=root
        level=0
        stack=[]
        while(curr or len(stack)>0):
            while(curr):
                if level>=len(lst): lst.append([1,curr.val])
                else: 
                    lst[level][1]=((lst[level][1]*lst[level][0])+curr.val)/(lst[level][0]+1)
                    lst[level][0]+=1
                stack.append((curr,level))
                curr=curr.left
                level+=1
            
            curr,level=stack.pop()
            curr=curr.right
            level+=1
        lst=[a[1] for a in lst]