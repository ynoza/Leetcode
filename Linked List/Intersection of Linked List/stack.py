# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stack1=[]
        stack2=[]
        while(headA or headB):
            if headA: 
                stack1.append(headA)
                headA=headA.next
            if headB:
                stack2.append(headB)
                headB=headB.next
        
        if len(stack1)==0 or len(stack2)==0: return None
        while(len(stack1)>0 and len(stack2)>0):
            curr1=stack1.pop()
            curr2=stack2.pop()
            if curr1==curr2: continue
            elif curr1.next == curr2.next: return curr1.next
            else: break
        if curr1: return curr1
        return None