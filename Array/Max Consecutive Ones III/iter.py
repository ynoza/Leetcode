# https://leetcode.com/problems/max-consecutive-ones-iii/submissions/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount=[]
        ret=0
        length=0
        for i, n in enumerate(nums):
            if n==0:
                zeroCount.append(i)
                if len(zeroCount)>k:
                    length=i-zeroCount.pop(0)
                else:
                    length+=1
            else:
                length+=1
            
            if length>ret: ret=length
            # print(ret)
        
        return ret
            
                    