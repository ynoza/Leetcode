# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lst=[]
        stack=[]
        curr=root
        while(curr or len(stack)>0):
            while(curr):
                lst.append(curr.val)
                stack.append(curr)
                if len(curr.children)>0:
                    curr=curr.children.pop(0)
                else: curr=None
            
            curr=stack.pop()
            if len(curr.children)>0:
                stack.append(curr)
                curr=curr.children.pop(0)
            else: curr=None
        return lst
                    