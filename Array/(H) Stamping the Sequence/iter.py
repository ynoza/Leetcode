# https://leetcode.com/problems/stamping-the-sequence/
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if stamp==target: return [0]
        S=list(stamp)
        T=list(target)
        slen=len(stamp)
        tlen=len(target)-slen+1
        ans=[]
        fir=True
        sec=True
        s=set()
        while fir:
            fir=False
            for i in range(tlen):
                sec=False
                for j in range(slen):
                    if T[i+j]=='*': continue
                    elif T[i+j]==S[j]: sec=True
                    else: break
                else:
                    if sec:
                        fir=True           
                        for j in range(i,i+slen):
                            s.add(j)
                            T[j]="*"
                        ans.append(i)
        
        if len(s)!=len(target): return []
        return reversed(ans)