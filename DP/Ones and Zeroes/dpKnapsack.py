# https://leetcode.com/problems/ones-and-zeroes/
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0 for i in range(n+1)] for i in range(m+1)]
        for s in strs:
            tM=0
            tN=0
            for c in s:
                if c=='0': tM+=1
                else: tN+=1
            
            for i in range(m,tM-1,-1):
                for j in range(n,tN-1,-1):
                    if dp[i][j]<dp[i-tM][j-tN]+1: dp[i][j]=dp[i-tM][j-tN]+1
            
        return dp[m][n]
            
                    
            
    