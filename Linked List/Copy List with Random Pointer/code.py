"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        hd={}
        start=head
        while(head):
            hd[head]=Node(head.val)
            head=head.next
            
        head=start

        while(head):
            if head.random: 
                hd[head].random=hd[head.random]
            if head.next:
                hd[head].next=hd[head.next]
            head=head.next
            
                
        return hd[start]