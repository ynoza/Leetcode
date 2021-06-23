class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d=defaultdict(int)
        for c in s:
            d[c]+=1
        
        ret=0
        for w in words:
            at=d
            bool=True
            for c in w:
                at[c]-=1
                if at[c]<0: 
                    bool=False
                    break
            if bool:
                ret+=1
        return ret