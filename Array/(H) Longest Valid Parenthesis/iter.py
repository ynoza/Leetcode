# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        maxCount=0
        for c in s:
            if c==')' and len(stack)>0: 
                val=stack.pop()
                if val=='(': 
                    count=2
                    while(len(stack)>0 and stack[-1]!=')' and stack[-1]!='('):
                        val=stack.pop()
                        count+=val
                    if maxCount<count: maxCount=count
                    stack.append(count)
                elif val!=')' and len(stack)>0:
                    val2=stack.pop()
                    if val2=='(':
                        count=val+2
                        while(len(stack)>0 and stack[-1]!=')' and stack[-1]!='('):
                            val=stack.pop()
                            count+=val
                        if maxCount<count: maxCount=count
                        stack.append(count)
                            
            elif c=='(': stack.append(c)
            # print(stack)
                
        return maxCount