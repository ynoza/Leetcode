# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        elif not head.next:
            return head
        first=head
        last=head.next
        keep=last
        start=first
        while(last and last.next):
            first.next=last.next
            last.next=first.next.next
            first=first.next
            last=last.next
        first.next=keep
        return start