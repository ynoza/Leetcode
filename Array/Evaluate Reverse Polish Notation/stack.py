# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else:
                val2=stack.pop()
                val1=stack.pop()
                if t=='-': stack.append(val1-val2)
                elif t=='+': stack.append(val1+val2)
                elif t=='/': stack.append(int(val1/val2))
                elif t=='*': stack.append(val1*val2)
                else: print("errrrrrrr")
        return stack[0]