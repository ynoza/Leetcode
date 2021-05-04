# https://leetcode.com/problems/non-decreasing-array/
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fD=False
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if fD:
                    return False
                elif i==1:
                    nums[i]=min(nums[i],nums[i-1])
                    nums[i-1]=min(nums[i],nums[i-1])
                elif nums[i-2]<=nums[i]: 
                    nums[i-1]=nums[i-2]
                else:
                    nums[i]=nums[i-1]
                fD=True
        return True
    
        