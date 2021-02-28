# https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0: return 0
        elif n==1: return 0
        ret=[True] * n
        
        for i in range(2,math.ceil(math.sqrt(n))):
            if ret[i]:
                for j in range(i*i,n,i):
                    ret[j]=False
        # print(ret)
        return sum(ret)-2
        