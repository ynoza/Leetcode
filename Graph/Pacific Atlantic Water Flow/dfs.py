# https://leetcode.com/problems/pacific-atlantic-water-flow/
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        valid=[]
        leftVisited=set()
        rightVisited=set()
        m=len(matrix)
        if m==0: return valid
        n=len(matrix[0])
        def dfs(visited,i,j):
            nonlocal m,n
            stack=[(i,j)]
            visited.add((i,j))
            while(len(stack)>0):
                i,j=stack.pop()
                if i-1>=0 and matrix[i][j]<=matrix[i-1][j] and (i-1,j) not in visited:
                    visited.add((i-1,j))
                    stack.append((i-1,j))

                if i+1<m and matrix[i][j]<=matrix[i+1][j] and (i+1,j) not in visited: 
                    visited.add((i+1,j))
                    stack.append((i+1,j))

                if j-1>=0 and matrix[i][j]<=matrix[i][j-1] and (i,j-1) not in visited: 
                    visited.add((i,j-1))
                    stack.append((i,j-1))

                if j+1<n and matrix[i][j]<=matrix[i][j+1] and (i,j+1) not in visited: 
                    visited.add((i,j+1))
                    stack.append((i,j+1))
            
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i<m-1 and j <n-1: continue
                elif (i,j) not in rightVisited:
                    dfs(rightVisited,i,j)
        
        for i in range(m):
            for j in range(n):
                if i>0 and j >0: continue
                elif (i,j) not in leftVisited:
                    dfs(leftVisited,i,j)

        for i in range(m):
            for j in range(n):
                if (i,j) in leftVisited and (i,j) in rightVisited:
                    valid.append([i,j])
                            
        return valid
                        