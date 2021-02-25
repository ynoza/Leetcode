# https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        start=head
        prev=None
        i=1
        while(i<left):
            prev=start
            start=start.next
            i+=1
            
        t1=None
        t2=start
        while(i<=right):
            temp=t2.next
            t2.next=t1
            t1=t2
            t2=temp
            i+=1
            
        start.next=t2
        if prev==None: return t1
        prev.next = t1
        
        return head
            