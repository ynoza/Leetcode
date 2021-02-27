# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        stack=[(0,0,[])]
        while(len(stack)>0):
            at,i,curr=stack.pop()
            if at==target:
                ret.append(curr)
                continue
            elif i==len(candidates):
                continue
            
            temp = (target-at) // candidates[i]
            while(temp>=0):
                stack.append([at+candidates[i]*temp,i+1,curr+[candidates[i]]*temp])
                temp-=1
        return ret