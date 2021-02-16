# https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        one=nums[0]
        min_val=float('inf')
        for i in range(1,len(nums)):
            if nums[i]>min_val: 
                return True
            elif nums[i]>one and min_val>nums[i]:
                min_val=nums[i]
            elif nums[i]<=one:
                one=nums[i]

        return False
    