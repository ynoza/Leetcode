# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        lst=[]
        while(head):
            lst.append(head.val)
            head=head.next
            
        def addNode(lstRem):
            if len(lstRem)==0: return None
            node = TreeNode(lstRem[len(lstRem)//2])
            node.left=addNode(lstRem[:len(lstRem)//2])
            node.right=addNode(lstRem[len(lstRem)//2+1:])
            return node

        return addNode(lst)