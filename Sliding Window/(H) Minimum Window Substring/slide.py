# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tLst=defaultdict(int)
        count=0
        for c in t:
            tLst[c]+=1
            count+=1
        
        starting=0
        minsofar=s+"6"
        countsofar=0

        for i in range(len(s)):
            c=s[i]
            if c in tLst:
                tLst[c]-=1
                if tLst[c]>=0: 
                    countsofar+=1
                while(starting<=i and (s[starting] not in tLst or tLst[s[starting]]<0)): 
                    if s[starting] in tLst: tLst[s[starting]]+=1
                    starting+=1 
            
            if countsofar==count:
                if len(minsofar) >= i-starting+1:
                    minsofar=s[starting:i+1]
                tLst[s[starting]]+=1
                starting+=1
                countsofar-=1
                
                while(starting<=i and (s[starting] not in tLst or tLst[s[starting]]<0)): 
                    if s[starting] in tLst: tLst[s[starting]]+=1
                    starting+=1 
                
            # print(c,countsofar,starting,minsofar)
        
        if len(minsofar)<=len(s): return minsofar
        return ""
                    
        