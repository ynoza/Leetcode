# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        elif n==1: return 1
        prev1=0
        prev2=1
        while(n>1):
            temp=prev2
            prev2=prev2+prev1
            prev1=temp
            n-=1
        return prev2