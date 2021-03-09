# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        levelList=[]
        def recur(root,level):
            nonlocal levelList
            if root==None: return
            elif level>=len(levelList): levelList.append(None)
            
            root.next=levelList[level]
            levelList[level]=root
            
            recur(root.right,level+1)
            recur(root.left,level+1)
        recur(root,0)
        return root