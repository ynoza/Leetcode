# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[[] for j in range(target+1)]
                
        while(len(candidates)>0):
            for c in range(candidates[-1],target+1):
                if c==candidates[-1]:
                    dp[c].append([c])
                else:
                    for d in dp[c-candidates[-1]]:
                        dp[c].append(d+[candidates[-1]])
            candidates.pop()
                        
        return dp[-1]
                