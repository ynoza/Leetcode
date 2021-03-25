# https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.valStack=[]
        self.curr=root
        self.stack=[]
        
    def next(self) -> int:
        if len(self.valStack)>0: return self.valStack.pop(0)
        
        while(self.curr):
            self.stack.append(self.curr)
            self.curr=self.curr.left
        self.curr=self.stack.pop()
        self.valStack.append(self.curr.val)
        self.curr=self.curr.right
        return self.valStack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.curr


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()