# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        Acount=0
        Bcount=0
        A=headA
        B=headB
        while(headA or headB):
            if headA: 
                Acount+=1
                headA=headA.next
            if headB:
                Bcount+=1
                headB=headB.next
        
        headA=A
        headB=B
        while(Acount>Bcount):
            headA=headA.next
            Acount-=1
        while(Bcount>Acount):
            headB=headB.next
            Bcount-=1
        
        while(headA):
            if headA==headB: return headA
            headA=headA.next
            headB=headB.next
        return None
        
