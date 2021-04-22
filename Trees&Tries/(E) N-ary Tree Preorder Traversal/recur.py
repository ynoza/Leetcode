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
        def recur(root):
            nonlocal lst
            if root==None: return
            for r in root.children:
                lst.append(r.val)
                recur(r)
        if root: lst.append(root.val)
        recur(root)
        return lst