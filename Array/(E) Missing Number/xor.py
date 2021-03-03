# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=len(nums)
        for i,val in enumerate(nums):
            ans^= (i^val)
        return ans