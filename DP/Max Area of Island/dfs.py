# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            nonlocal grid
            stack=[(i,j)]
            area=0
            while(len(stack)>0):
                curr=stack.pop()
                area+=1
                if curr[0]+1<len(grid) and grid[curr[0]+1][curr[1]]==1:
                    stack.append((curr[0]+1,curr[1]))
                    grid[curr[0]+1][curr[1]]=0
                if curr[0]-1>=0 and grid[curr[0]-1][curr[1]]==1:
                    stack.append((curr[0]-1,curr[1]))
                    grid[curr[0]-1][curr[1]]=0
                if curr[1]+1<len(grid[0]) and grid[curr[0]][curr[1]+1]==1:
                    stack.append((curr[0],curr[1]+1))
                    grid[curr[0]][curr[1]+1]=0
                if curr[1]-1>=0 and grid[curr[0]][curr[1]-1]==1:
                    stack.append((curr[0],curr[1]-1))
                    grid[curr[0]][curr[1]-1]=0
            return area
        
        ret=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0
                    ret=max(ret, dfs(i,j))
                    # print(i,j,grid)
        return ret
                    