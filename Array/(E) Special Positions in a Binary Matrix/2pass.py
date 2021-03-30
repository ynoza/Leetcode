# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0

        r=[0]*len(mat)
        c=[0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                c[j] +=mat[i][j]
                r[i] +=mat[i][j]
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and c[j]==1 and r[i]==1: count+=1
           
        return count
                
                    
        