# https://leetcode.com/problems/maximum-gap/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ret=0
        nums=sorted(nums)
        for i,n in enumerate(nums):
            if i>0: ret=max(ret,nums[i]-nums[i-1])
        return ret