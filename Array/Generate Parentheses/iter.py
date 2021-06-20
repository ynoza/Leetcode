# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[["(",1,0]]
        for i in range(2,n+1):
            # newLst=[]
            start=len(lst)
            for k in range(start):
                l=lst[k]
                for j in range(l[1]-l[2]+1):
                    lst.append(l.copy())
                    lst[-1][0]+=(j * ")")
                    lst[-1][2]+=j
                    
                    lst[-1][0]+=('(')
                    lst[-1][1]+=1
            # lst=newLst
            lst=lst[start:]
        
        ret=[]
        for l in lst: ret.append(l[0]+((l[1]-l[2])*")"))
            
        return ret
    
    
        