class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            if i==0 and i+1<len(nums) and nums[i]>nums[i+1]: return i
            elif i==len(nums)-1 and i-1>=0 and nums[i]>nums[i-1]: return i
            
            if nums[i-1]< nums[i] and nums[i]>nums[i+1]: return i
        return -1
            

        
        