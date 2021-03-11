# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=len(nums)
        if l==0: return 0
        elif l==1: return 1
        nums=list(set(nums))
        nums.sort()
        # print(nums)
        val=nums[0]
        max_count=1
        count=1
        for i in range(1,len(nums)):
            if nums[i]==val+1: 
                count+=1
            else: 
                max_count=max(max_count,count)
                count=1
            val = nums[i]
        max_count=max(max_count,count)
        return max_count
        
        