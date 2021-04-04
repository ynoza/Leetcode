# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l,r=0,0
        maxCount=0
        for c in s:
            if c==')':
                r+=1
            else:
                l+=1
            
            if l==r: 
                maxCount=max(maxCount,r*2)
            elif r>l:
                r,l=0,0
        
        l,r=0,0
        for i in range(len(s)-1,-1,-1):
            c=s[i]
            if c==')':
                r+=1
            else:
                l+=1
            
            if l==r: 
                maxCount=max(maxCount,l*2)
            elif r<l:
                r,l=0,0
        return maxCount