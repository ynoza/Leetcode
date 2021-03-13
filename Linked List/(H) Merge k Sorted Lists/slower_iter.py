# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head=None
        start=head

        while(True):
            at=None
            index=[]
            for i,l in enumerate(lists):
                if l!=None:
                    if at==None: 
                        at=l
                        index=[i]
                    elif at.val==l.val: 
                        at=l
                        index.append(i)
                    elif at.val>l.val:
                        at=l
                        index=[i]
            
            if at==None: return start
            elif head==None: 
                head=at
                start=head
                lists[index[-1]]=lists[index[-1]].next
            
            for ind in index:
                while(lists[ind]!=None and lists[ind].val==at.val):
                    head.next=lists[ind]
                    head=head.next
                    lists[ind]=lists[ind].next
            
        return start