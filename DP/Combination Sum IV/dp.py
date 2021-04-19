# https://leetcode.com/problems/combination-sum-iv/
from math import comb
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0 for i in range(target+1)]
        nums.sort()
        dp[0]=1
        for t in range(len(dp)):
            for i,n in enumerate(nums):
                if n>t: break
                dp[t]+=dp[t-n]
        return dp[target]