# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=(matrix[i][j],0)
                
        def dfs(i,j):
            nonlocal matrix
            if matrix[i][j][1]>0: return matrix[i][j][1]
            
            lst=[]
            if i-1>=0 and matrix[i-1][j][0]<matrix[i][j][0]:
                lst.append((i-1,j))
            if j-1>=0 and matrix[i][j-1][0]<matrix[i][j][0]:
                lst.append((i,j-1))
            if i+1<len(matrix) and matrix[i+1][j][0]<matrix[i][j][0]:
                lst.append((i+1,j))
            if j+1<len(matrix[0]) and matrix[i][j+1][0]<matrix[i][j][0]:
                lst.append((i,j+1))
            
            if len(lst)==0: return 0
            
            val=0
            for l in lst:
                temp= 1 + dfs(l[0],l[1])
                if val < temp: val=temp
                
            matrix[i][j]=(matrix[i][j][0],val)
            return val
        
            
        maxVal=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = dfs(i,j)
                # print(i,j,val)
                if maxVal<1+val:
                    maxVal=1+val
                
        return maxVal