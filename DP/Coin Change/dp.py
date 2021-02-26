# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount==0): return 0
        # coins.sort()
        
        dp=[]
        dp.append(0)
        for i in range(1,amount+1):
            val=float('inf')
            for x in coins:
                if (i-x<0): pass
                elif dp[i-x]+1<val: val=dp[i-x]+1
            dp.append(val)
        
        # print(dp)
        if dp[-1]==float('inf'): return -1
        else: return dp[-1]
        