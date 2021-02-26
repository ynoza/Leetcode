# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=dict()
        count=0
        for i in nums:
            if k-i in d:
                d[k-i]-=1;
                count+=1
                if d[k-i]==0: del d[k-i]
            elif i in d:
                d[i]+=1
            else:
                d[i]=1
        return count