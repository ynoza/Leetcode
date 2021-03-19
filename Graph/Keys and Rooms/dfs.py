# https://leetcode.com/problems/keys-and-rooms/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        stack=[rooms[0]]
        visited.add(0)
        while(len(stack)>0):
            curr=stack.pop()
            # print(curr)
            for num in curr: 
                if num not in visited:
                    stack.append(rooms[num])
                    visited.add(num)
                if len(visited)==len(rooms): return True
        return len(visited)==len(rooms)