# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev=float('-inf')
        maxsofar=float('-inf')
        for i in range (len(nums)):
            if i==0:
                maxsofar=nums[0]
                prev=nums[0]
            else:
                if nums[i] >= prev+nums[i]: prev=nums[i]
                else: prev=prev+nums[i]
                
                if maxsofar<prev: maxsofar=prev
        return maxsofar
        