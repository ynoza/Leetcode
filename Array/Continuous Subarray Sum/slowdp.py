# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp=[]
        for j in range(1,len(nums)):
            for i in range(len(nums)-j):
                if j==1: dp.append(nums[i])
                dp[i]+=nums[i+j]
                if k==0:
                    if dp[i]==0: return True
                elif dp[i]%k==0: return True
        return False
