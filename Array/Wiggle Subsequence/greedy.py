# https://leetcode.com/problems/wiggle-subsequence/
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count=1
        at=nums[0]
        Inc=True
        Dec=True
        for i in range(len(nums)):
            if count==1 and nums[i]> at:
                at=nums[i]
                Inc=False
                count+=1
            elif count==1 and nums[i]< at:
                at=nums[i]
                Dec=False
                count+=1
            elif (Inc and nums[i]>at) or (Dec and nums[i]<at):
                count+=1
                at=nums[i]
                Inc=not Inc
                Dec=not Dec
            else:
                at=nums[i]
                
        return count