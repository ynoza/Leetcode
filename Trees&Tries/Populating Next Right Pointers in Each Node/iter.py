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
        stack=[]
        curr=root
        level=0
        while(curr or len(stack)>0):
            while(curr):
                if level>=len(levelList): levelList.append(None)
                curr.next=levelList[level]
                levelList[level]=curr
                stack.append((curr,level))
                level+=1
                curr=curr.right
            
            curr,level=stack.pop()
            curr=curr.left
            level+=1
        return root