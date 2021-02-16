# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        s+='1'
        stack=[]
        for i in range(len(s)):
            if len(stack)==0: stack.append(s[i])
            elif s[i]=='}' or s[i]==')' or s[i]==']':
                temp=stack.pop()
                if s[i]==')' and temp!='(': return False
                elif s[i]==']' and temp!='[': return False
                elif s[i]=='}' and temp!='{': return False
            else:
                stack.append(s[i])
        
        if len(stack)!=1 or  stack[0]!='1':
            return False
        return True