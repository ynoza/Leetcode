#https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ret=0
        median=nums[len(nums)//2]
        for n in nums:
            ret+=abs(median-n)
        return ret
    
        