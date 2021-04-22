# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l=len(triangle)
        for k in range(len(triangle)-1,-1,-1):
            t=triangle[k]
            if k==l-1: continue
            for i in range(len(t)):
                val1=triangle[k+1][i]
                val2=triangle[k+1][i+1]
                if val1 < val2:
                    triangle[k][i]+=val1
                else:
                    triangle[k][i]+=val2
        return triangle[0][0]
            