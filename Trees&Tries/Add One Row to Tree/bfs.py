# https://leetcode.com/problems/add-one-row-to-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d==1:
            n=TreeNode(v)
            n.left=root
            return n
        queue=[(root,1)]
        level=0
        while(len(queue)>0):
            curr,level=queue.pop(0)
            if curr==None: continue
            if level+1==d:
                l=TreeNode(v)
                r=TreeNode(v)
                l.left=curr.left
                curr.left=l
                r.right=curr.right
                curr.right=r
            else:
                queue.append((curr.left,level+1))
                queue.append((curr.right,level+1))
        return root
            