# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count=0
        temp=0
        upperBound=0
        previousInValid=-1
        for i,n in enumerate(nums):
            
            if (n>=left and n<=right):
                count+=i-previousInValid
                upperBound=i
                temp+=1
            elif n>right:
                previousInValid=i
                temp=0
            elif temp>0:
                count+=upperBound-previousInValid
            
        return count
    