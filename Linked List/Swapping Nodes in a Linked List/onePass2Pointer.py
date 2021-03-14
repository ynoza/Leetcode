# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if head==None: return None
        elif head.next==None: return head
        ret=head
        
        count=1
        while(count+1<k):
            count+=2
            head=head.next.next
        if count!=k: 
            count+=1
            head=head.next
            
        temp_start=count
        start=head
        beg=ret
        
        while(head.next):
            if head.next.next:
                head=head.next.next
                beg=beg.next.next
            else:
                head=head.next
                beg=beg.next
        
        # print(start.val,head,beg)
        
        temp1=start.val
        start.val=beg.val
        beg.val=temp1
        
        return ret