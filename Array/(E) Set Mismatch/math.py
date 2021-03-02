# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s_sum, val=sum(set(nums)), (n*(n+1))//2
        nums_sum,missing=sum(nums), val-s_sum
        return [nums_sum+missing-val, missing]
            