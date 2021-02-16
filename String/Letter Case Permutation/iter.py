# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        x=[]
        stack=[(S,"")]
        while(len(stack)>0):
            s,perm=stack.pop()
            if s=="": 
                x.append(perm)
                continue
            if s[0].islower():
                stack.append((s[1:], perm + s[0].upper()))
            elif s[0].isupper():
                stack.append((s[1:], perm + s[0].lower()))
            stack.append((s[1:], perm + s[0]))
            
        return x