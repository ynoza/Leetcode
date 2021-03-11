# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for k in range(n): 
                        if matrix[i][k]!=0: matrix[i][k]=6969
                    for k in range(m): 
                        if matrix[k][j]!=0: matrix[k][j]=6969
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==6969: matrix[i][j]=0