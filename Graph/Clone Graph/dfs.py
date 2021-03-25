# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None: return None
        visited=dict()
        visited[node.val]=Node(node.val)
        stack=[(visited[node.val],node)]
        while(len(stack)>0):
            curr,org=stack.pop()
            for neigh in org.neighbors:
                if neigh.val not in visited:
                    visited[neigh.val]=Node(neigh.val)
                    stack.append((visited[neigh.val],neigh))
                curr.neighbors.append(visited[neigh.val])

        return visited[node.val]