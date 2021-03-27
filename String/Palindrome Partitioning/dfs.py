# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        # ret=[]
        count=0
        def dfs(l,r):
            nonlocal count, s
            stack=[(l,r)]
            while(len(stack)>0):
                l,r=stack.pop()
                if l<0 or r>=len(s): continue
                elif s[l]!=s[r]: continue
                count+=1
                stack.append((l-1,r+1))
        
        stack=[]
        for i in range(len(s)):
            count+=1
            dfs(i-1,i+1)
            if i+1<len(s) and s[i]==s[i+1]:
                count+=1
                dfs(i-1,i+2)

        return count
                    
                    