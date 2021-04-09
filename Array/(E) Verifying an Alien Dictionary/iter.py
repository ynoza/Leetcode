# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d=dict()
        for i,c in enumerate(order):
            d[c]=i
        
        i=0
        while(True):
            prev=None
            for j,w in enumerate(words):
                if i >len(w): continue
                elif i==len(w):
                    if prev!=None: return False
                elif prev==None: prev=j
                elif d[w[i]]<d[words[prev][i]]: return False
                elif d[w[i]]>d[words[prev][i]]: 
                    words[prev]=""
                    prev=j
                else: prev=j
                    
            if prev==None: return True
            i+=1
        return True