class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]
        for i in range(1,len(nums)):
            ans.append(ans[-1]*(nums[i-1]))
        # print(ans)
        L=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=L
            L*=nums[i]
        return ans