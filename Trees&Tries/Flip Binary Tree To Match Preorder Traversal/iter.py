# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        lst=[]
        if root==None: 
            return []
        elif root.val!=voyage[0]: 
            return [-1]
        voyage.pop(0)
        stack=[]
        curr=root
        while(curr or len(stack)>0):
            while(curr):
                if curr.left and curr.right:
                    if curr.left.val == voyage[0]: voyage.pop(0)
                    elif voyage[0]==curr.right.val:
                        temp=curr.left
                        curr.left=curr.right
                        curr.right=temp
                        lst.append(curr.val)
                        voyage.pop(0)
                    else: return [-1]
                elif curr.left:
                    if curr.left.val!=voyage[0]: 
                        return [-1]
                    voyage.pop(0)
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop()
            
            
            if curr.right:
                if curr.right.val!=voyage[0]: 
                    return [-1]
                voyage.pop(0)
                
            curr=curr.right
        
        return lst