# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0: return False
        elif n<0: return False
        elif n==1: return True
        l=0
        r=min(n//3,19)
        while (l<=r):
            mid=(l+r)//2
            val=math.pow(3,mid)
            #print(mid,val)
            if val==n: return True
            elif val>n: r=mid-1
            else: l=mid+1
        return False