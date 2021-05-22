# https://leetcode.com/problems/find-and-replace-pattern/
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def doMatching(word):
            nonlocal pattern
            dic=dict()
            s=set()
            for i,c in enumerate(pattern):
                if c in dic:
                    if dic[c]!=word[i]: return False
                    
                elif word[i] not in s: 
                    dic[c]=word[i]
                    s.add(word[i])
                else:
                    return False
            return True
        
        ret=[]
        for w in words:
            if doMatching(w): ret.append(w)
                
        return ret