# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        change=False
        if n<0:
            change=True
            n=-1*n
        rx=abs(x)
        def recur(t):
            if (t==0): return 1
            temp =  recur(t//2)
            return temp*temp*rx if t % 2 else temp*temp
        
        ret = recur(n)
        if change: ret=1/ret
        if x<0 and n%2==1: return -1*ret
        return ret