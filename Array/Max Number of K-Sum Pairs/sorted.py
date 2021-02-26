# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        l=0
        r=len(nums)-1
        while(l<r):
            val=nums[l]+nums[r]
            if val==k: 
                l+=1
                r-=1
                count+=1
            elif val>k:
                r-=1
            else:
                l+=1
        return count