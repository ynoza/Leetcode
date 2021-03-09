# https://leetcode.com/problems/remove-palindromic-subsequences/
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n=len(s)
        if n==0: return 0
        n-=1
        l=0
        while (l<n):
            if s[l]!= s[n]: return 2
            l+=1
            n-=1
        return 1