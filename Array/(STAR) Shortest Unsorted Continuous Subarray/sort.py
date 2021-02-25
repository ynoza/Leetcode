# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        t=sorted(nums)
        start=-1
        end=-1
        for i in range(len(nums)):
            if start==-1 and nums[i]!=t[i]:
                start=i
            if end==-1 and nums[len(nums)-1-i]!=t[len(nums)-1-i]:
                end=len(nums)-1-i
            if start!=-1 and end!=-1:
                # print(start,end)
                return end-start+1
        return 0