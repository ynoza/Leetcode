# https://leetcode.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if (len(popped)==0): return True
        j=0
        stack=[]
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while(len(stack)>0 and stack[-1]==popped[j]):
                j+=1
                stack.pop()
        if j==len(popped): return True
        return False
                