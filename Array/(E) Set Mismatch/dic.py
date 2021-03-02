# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d=dict()
        s=0
        val=(n*(n+1))//2
        check=True
        ans=-1
        for i in range(n):
            s+=nums[i]
            if check:
                if nums[i] not in d:
                    d[nums[i]]=True
                else:
                    ans=nums[i]
                    check=False
        s-=ans
        return [ans,val-s]
            
            