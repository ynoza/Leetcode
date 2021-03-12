# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=len(nums)
        if l==0: return 0
        elif l==1: return 1
        
        nums=set(nums)
        maxsofar=1
        for num in nums:
            if num-1 not in nums:
                at=num
                s=1
                while(at+1 in nums):
                    at+=1
                    s+=1
                if s>maxsofar: maxsofar=s
        return maxsofar
        
        