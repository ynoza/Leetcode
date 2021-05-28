# https://leetcode.com/problems/maximum-product-of-word-lengths/
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words=sorted(words,key=len,reverse=True)
        for i in range(len(words)):
            dic=Counter(words[i])
            words[i]=dic
        ret=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                exists=False
                for c in words[i].keys():
                    if c in words[j]: 
                        exists=True
                        break
                if not exists: ret=max(ret,sum(words[i].values())*sum(words[j].values()))
                
        return ret
        
                