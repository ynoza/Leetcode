# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup=-1
        nums=[-1]+nums
        s=0
        for i in range(1,len(nums)):
            a=abs(nums[i])
            s+=a
            if nums[a]<0:
                dup=a
            nums[a]*=-1
            # print(nums)
        n=len(nums)
        val=((n-1)*(n))//2
        s-=dup
        return [dup,val-s]
            
            