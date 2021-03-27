# https://leetcode.com/problems/word-subsets/
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ret=[]
        realDictionary = defaultdict(int)
        for w in B:
            tempD=defaultdict(int)
            for c in w:
                tempD[c]+=1
                if tempD[c]>realDictionary[c]:
                    realDictionary[c]+=1
        
        for w in A: 
            d=defaultdict(int)
            t=True
            for c in w:
                d[c]+=1
            
            for k,v in realDictionary.items():
                if d[k]<v: 
                    t=False
                    break
            if t: ret.append(w)
        return ret