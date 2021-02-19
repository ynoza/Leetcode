# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ret=""
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(('(',i))
            elif s[i]==')':
                if len(stack)>0 and stack[-1][0]=='(': stack.pop()
                else: stack.append((')',i))

            # print(s[i],stack)
        while(len(stack)>0):
            ch,i=stack.pop()
            s=s[:i]+s[i+1:]
        return s