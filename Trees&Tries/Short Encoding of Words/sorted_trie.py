# https://leetcode.com/problems/short-encoding-of-words/
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words=list(set(words))
        words=sorted(words, key=len,reverse=True)
        # print(words)
        suffix={}
        count=0
        for w in words:
            at=suffix
            h=0
            for i in range(len(w)-1,-1,-1):
                c=w[i]
                h+=1
                if c in at: 
                    at=at[c]                   
                else:
                    at[c]={}
                    at=at[c]
            if len(at.keys())==0: count+=(h+1)
        # print(suffix)
        return count
            