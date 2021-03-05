# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        po=5
        ans=0
        while(po <= n):
            ans+= n // po
            po*=5
            
        return ans