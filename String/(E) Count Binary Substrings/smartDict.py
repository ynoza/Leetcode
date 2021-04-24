# https://leetcode.com/problems/count-binary-substrings/
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr=defaultdict(int)
        prev=defaultdict(int)
        at=None
        count=0
            
        for c in s:
            if at==None:
                at=c
                curr[at]+=1
            elif c==at:
                curr[at]+=1
            else:
                if at=="0": count+=min(prev["1"],curr["0"])
                elif at=="1": count+=min(prev["0"],curr["1"])
                prev[at]=curr[at]
                curr[at]=0
                at=c
                curr[at]=1
                prev[at]=0
                
        if at=="0": count+=min(prev["1"],curr["0"])
        elif at=="1": count+=min(prev["0"],curr["1"])
        return count
    
    