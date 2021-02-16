# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[1 for _ in range(n)] for _ in range (m)]
        maxsofar=0
        for i in range(m):
            for j in range(n):
                if dp[i][j]==1:
                    stack=[(i,j,1)]
                    while(len(stack)>0):
                        a,b,count=stack.pop()
                        dp[a][b]=max(dp[a][b],count)
                        at=matrix[a][b]
                        if a+1<m and matrix[a+1][b]<at and dp[a+1][b]<count+1: 
                            stack.append((a+1,b,count+1)) 
                        if b+1<n and matrix[a][b+1]<at and dp[a][b+1]<count+1: 
                            stack.append((a,b+1,count+1)) 
                        if a-1>=0 and matrix[a-1][b]<at and dp[a-1][b]<count+1: 
                            stack.append((a-1,b,count+1)) 
                        if b-1>=0 and matrix[a][b-1]<at and dp[a][b-1]<count+1: 
                            stack.append((a,b-1,count+1)) 
        
        for i in range (m):
            maxsofar=max(maxsofar,max(dp[i]))

        return maxsofar