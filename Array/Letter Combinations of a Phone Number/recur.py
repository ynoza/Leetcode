# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0: return []
        d=[0,0,"abc","def","ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def recur (s,path,x):
            nonlocal d
            if s=="": 
                x.append(path)
                return
            for c in d[int(s[0])]:
                recur(s[1:], path+ c,x)
        x=[]
        recur(digits,"",x)
        return x