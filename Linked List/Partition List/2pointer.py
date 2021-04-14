# https://leetcode.com/problems/partition-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lower_half=None
        upper_half=None
        lower_start=None
        upper_start=None
        while(head):
            if head.val<x:
                if lower_half:
                    lower_half.next=head
                    lower_half=lower_half.next
                else:
                    lower_half=head
                    lower_start=head
            elif upper_half:
                upper_half.next=head
                upper_half=upper_half.next
            else:
                upper_half=head
                upper_start=head
            head=head.next
        
        if not lower_start: return upper_start
        if upper_half: upper_half.next=None
        lower_half.next=upper_start
        return lower_start