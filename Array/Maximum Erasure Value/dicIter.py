# https://leetcode.com/problems/maximum-erasure-value/
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic=dict()
        ret=0
        leftInd=0
        left=[0]
        for i in range(len(nums)):
            left.append(left[-1]+nums[i])
                
            if nums[i] in dic:
                tempVal = left[i]-left[leftInd+1]+nums[leftInd]
                if ret < tempVal: ret= tempVal
                # print(ret, dic[nums[i]],i)
                temp=dic[nums[i]]
                for j in range(leftInd, temp+1):
                    del dic[nums[j]]
                leftInd=temp+1
                # print(leftInd)
            dic[nums[i]]=i
        
        tempVal = left[len(nums)]-left[leftInd+1]+nums[leftInd]
        if ret< tempVal:
            ret = tempVal
        
        return ret