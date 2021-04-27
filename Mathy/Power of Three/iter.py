# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        elif n==0:
            return False
        elif n==-1:
            return True
        elif n<0:
            return False
        while(n>1):
            rem=n%3
            if (rem!=0):
                return False
            n=n//3
        
        return True