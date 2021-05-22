#https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def findHeight(root):
            if root==None: return 0
            return max(findHeight(root.left),findHeight(root.right))+1
        
        heightOfSubTree=findHeight(subRoot)
        ret=False
        
        def match(root,subRoot):
            if root==None and subRoot==None: return True
            elif root==None: return False
            elif subRoot==None: return False
            elif root.val!=subRoot.val: return False
            return match(root.left,subRoot.left) and match (root.right,subRoot.right)
        
        
        def recur(root):
            nonlocal heightOfSubTree,ret,subRoot
            if root==None: return 0
            height=max(recur(root.left), recur(root.right))+1
            
            if height==heightOfSubTree:
                ret|=match(root,subRoot)
                # print("ran match")
            return height
        
        # print(heightOfSubTree)
        recur(root)
        return ret