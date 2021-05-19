# https://leetcode.com/problems/binary-tree-cameras/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minCameraCover(self, root: TreeNode) -> int:
        count=0
        
        def recur(root):
            nonlocal count
            if root==None: return

            recur(root.left)
            recur(root.right)
            if (root.left and root.left.val==0) or (root.right and root.right.val==0):
                root.val=1
                count+=1
            elif (root.left and root.left.val==1) or (root.right and root.right.val==1):
                root.val=2
            
        news=TreeNode(0)
        news.left=root
        recur(news)
        # if root and not root.right and not root.left: count+=1
        
        return count
            
            