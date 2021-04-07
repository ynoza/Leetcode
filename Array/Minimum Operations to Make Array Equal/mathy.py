# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
class Solution:
    def minOperations(self, n: int) -> int:
        mid=1
        ret=0
        l=0
        if n==1: return 0
        elif n==2: return 1
        elif n%2==1:
            mid=int(n/2)*2+1
            l=math.ceil(n/2)
        else:
            mid=int(n/2)*2
            ret+=1
            l=math.ceil(n/2)+1

        for i in range(l,n):
            ret+=(2*i+1-mid)
        return ret
        
        
        
        