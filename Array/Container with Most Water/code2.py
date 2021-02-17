# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxsofar=0
        while (l<=r):
            maxsofar=max(maxsofar,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]: l+=1
            else: r-=1
        
        return maxsofar