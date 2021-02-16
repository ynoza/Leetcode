# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def recur (s, perm, x):
            if (s==""): 
                x.append(perm)
                return
            if s[0].islower():
                recur (s[1:], perm + s[0].upper(), x)
            elif s[0].isupper():
                recur (s[1:], perm + s[0].lower(), x)
            recur (s[1:], perm + s[0], x)
        
        ret=[]
        recur(S,"",ret)
        return ret