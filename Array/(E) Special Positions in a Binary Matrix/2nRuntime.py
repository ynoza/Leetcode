# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(i,j):
            nonlocal mat
            for t in range(len(mat)):
                if t==i: continue
                elif mat[t][j]: return False,t
            
            return True,'n'
        
        count=0
        l=0
        dd=set()
        for i in range(len(mat)):
            val = sum(mat[i])
            if val > 1 or val < 1: continue
                
            for j in range(l,len(mat[0])):
                if mat[i][j]==1 and j not in dd:
                    b,c = check(i,j)
                    if b:
                        count+=1
                        dd.add(j)
                        break
                    else: 
                        dd.add(j)
            while(l<len(mat[0]) and l in dd): l+=1
        return count
                
                    
        
                
                    
        