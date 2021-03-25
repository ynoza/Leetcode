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
        length=0
        while(head):
            length+=1
            head=head.next
            
        if length<=2: return start
        
        head=start
        prev=None
        for i in range(length//2+2):
            prev=head
            head=head.next
        prev.next=None
        
        while(head):
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        
        head=start
        # print(prev)
        while(prev):
            temp2=head.next
            head.next=prev
            temp=prev.next
            prev.next=temp2
            head=temp2
            prev=temp
        if length%2==1: head.next=None
        else: head.next.next=None
        return start
            