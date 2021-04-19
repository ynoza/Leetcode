# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack=[]
        start=head
        while(head):
            stack.append(head)
            head=head.next
        
        prev=None
        while(len(stack)>0):
            temp=stack.pop()
            n-=1
            if n==0:
                if len(stack)==0:
                    temp=None
                    start=prev
                else:
                    stack.pop().next=prev    
            prev=temp
        return start