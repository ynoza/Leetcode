# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q=[]
        heapq.heapify(q)
        head=ListNode(0)
        start=head
        count=0
        for l in lists:
            if l:
                heapq.heappush(q,(l.val,count,l))
                count+=1
        
        while len(q)>0:
            val,useless,node = heapq.heappop(q)
            head.next=node
            head=head.next
            if node.next:
                heapq.heappush(q,(node.next.val,count,node.next))
                count+=1
            
        return start.next