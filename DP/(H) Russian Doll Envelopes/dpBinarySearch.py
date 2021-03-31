# https://leetcode.com/problems/russian-doll-envelopes/
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes=sorted(envelopes, key=lambda x: (x[0],-x[1]))
        dp=[]
        def doBin(n):
            nonlocal dp
            le=len(dp)
            l=0
            r=le-1
            while(l<=r):
                m=int((l+r)/2)
                if m>0 and dp[m-1]<n and dp[m]>=n: 
                    return m
                elif dp[m]>=n: r=m-1
                else: l=m+1
            return l
        
        count=0
        for i,n in enumerate(envelopes):
            x,y=n[0],n[1]
            val=bisect_left(dp,y) # can call doBin, but bisect_left is faster
            if val==len(dp): 
                dp.append(y)
                count+=1
            else:
                dp[val]=y
                
        return count