# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr=sorted(arr)
        res=[]
        def solve(i, curr_path, at):
            if at==0:
                res.append(curr_path)
                return
            elif i==len(arr): return
            elif arr[i]>at: return
            
            for j in range(i,len(arr)):
                solve(j, curr_path+[arr[j]], at-arr[j])
                
		# In order to avoid duplicates, we use a set
        res = []
        solve(0, [], target)
        return res