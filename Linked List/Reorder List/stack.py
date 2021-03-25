# https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start=head
        stack=[]
        length=0
        while(head):
            length+=1
            stack.append(head)
            head=head.next
        head=start
        prev=None
        while(head and head.next and head.next.next and head.next!=prev):
            temp=head.next
            head.next=stack[-1]
            head.next.next=temp
            prev=stack.pop()
            head=head.next.next
            # print(head.val)
        if length%2==1:
            head.next=None
        else:
            head.next.next=None
        return start
            