# https://leetcode.com/problems/maximum-erasure-value/
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # left=[0]
        right=[0]
        for i in range(len(nums)-1,-1,-1):
            right.append(nums[i]+right[-1])
        
        # left=left[1:]
        right=right[1:]
        right.reverse()
        # print(right)
        # print(left,right)
        
        dic=dict()
        ret=0
        leftInd=0
        for i in range(len(nums)):
            if nums[i] in dic:
                tempVal = right[leftInd]-right[i-1]+nums[i-1]
                if ret < tempVal: ret= tempVal
                # print(ret, dic[nums[i]],i)
                temp=dic[nums[i]]
                for j in range(leftInd, temp+1):
                    del dic[nums[j]]
                leftInd=temp+1
                # print(leftInd)
            dic[nums[i]]=i
    
        if ret< right[leftInd]:
            ret = right[leftInd]
        
        return ret