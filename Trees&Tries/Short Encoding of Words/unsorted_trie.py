# https://leetcode.com/problems/short-encoding-of-words/
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        suffix={}
        count=0
        for w in words:
            at=suffix
            h=0
            for c in w[::-1]:
                h+=1
                if c in at: 
                    at=at[c]
                    continue
                elif -1 in at and len(at.keys())==1:
                    count-=(h)                       
                at[c]={}
                at=at[c]
            if len(at.keys())>0: continue
            at[-1]={}
            count+=(h+1)
        return count
            