# https://leetcode.com/problems/find-latest-group-of-size-m/
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m
        n = len(arr)
        ret=[0]*(n+2)
        
        ans=-1
        for i in range(n):
            at=arr[i]
            val1=ret[at-1]
            val2=ret[at+1]
            if val1==m or val2==m: ans=i
            total=val1+val2+1
            ret[at-val1]=total
            ret[at+val2]=total
                     
        return ans