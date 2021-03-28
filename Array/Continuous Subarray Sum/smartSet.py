# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumsofar=0
        prev=0
        d=set()
        for i in range(len(nums)):
            sumsofar+=nums[i]
            if k!=0: sumsofar%=k
            if sumsofar in d: return True
            d.add(prev)
            prev=sumsofar
        return False
