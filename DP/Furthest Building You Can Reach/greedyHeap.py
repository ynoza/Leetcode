# https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights)==1: return 0
        
        sumSoFar=0
        temp=[]
        heapq.heapify(temp)
        for i in range(len(heights)-1):
            val=heights[i+1]-heights[i]
            sumSoFar+=max(0,val)
            heapq.heappush(temp,-val)
            if sumSoFar>bricks:
                if ladders==0: 
                    return i
                else: 
                    sumSoFar-=-1*heapq.heappop(temp)
                    ladders-=1
            # print(sumSoFar)
        return len(heights)-1
            