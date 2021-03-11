# https://leetcode.com/problems/surrounded-regions/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        if m<=1 or n<=1: return board
        visited=set()
        
        def dfs(i,j):
            nonlocal m,n,visited
            stack=[(i,j)]
            while(len(stack)>0):
                i,j=stack.pop()
                if i-1>=0 and board[i-1][j]=="O" and (i-1,j) not in visited: 
                    visited.add((i-1,j))
                    stack.append((i-1,j))
                if i+1<m and board[i+1][j]=="O" and (i+1,j) not in visited:
                    visited.add((i+1,j))
                    stack.append((i+1,j))
                if j-1>=0 and board[i][j-1]=="O" and (i,j-1) not in visited:
                    visited.add((i,j-1))
                    stack.append((i,j-1))
                if j+1<n and board[i][j+1]=="O" and (i,j+1) not in visited:
                    visited.add((i,j+1))
                    stack.append((i,j+1))
                        
        for i in [0,m-1]:
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    dfs(i,j)
                        
        for i in range(m):
            for j in [0,n-1]:
                if board[i][j] == "O" and (i,j) not in visited:
                    dfs(i,j)
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if (i,j) not in visited: board[i][j]="X"
        