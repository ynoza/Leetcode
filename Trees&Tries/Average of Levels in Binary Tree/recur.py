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
        def recur(root,level):
            if root==None:
                return
            if level>=len(lst): lst.append((1,root.val))
            else: 
                lst[level]=(lst[level][0]+1,((lst[level][1]*lst[level][0])+root.val)/(lst[level][0]+1))
            recur(root.left,level+1)
            recur(root.right,level+1)
        recur(root,0)
        lst=[a[1] for a in lst]
        return lst