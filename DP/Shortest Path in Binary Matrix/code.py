# https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid)==0: return -1
        elif grid[0][0]!=0: return -1 
        
        queue=[((0,0),0)]
        
        n=len(grid)
        m=len(grid[0])
        
        while(len(queue)>0):
            curr,num = queue.pop(0)
            if curr[0]==n-1 and curr[1]==m-1: return num+1
            temp=[]
            if curr[0]-1>=0:
                if grid[curr[0]-1][curr[1]]==0: temp.append((curr[0]-1,curr[1]))
                if curr[1]-1>=0 and grid[curr[0]-1][curr[1]-1]==0: temp.append((curr[0]-1,curr[1]-1))
                if curr[1]+1<m and grid[curr[0]-1][curr[1]+1]==0: temp.append((curr[0]-1,curr[1]+1))
            if curr[0]+1<n:
                if grid[curr[0]+1][curr[1]]==0: temp.append((curr[0]+1,curr[1]))
                if curr[1]-1>=0 and grid[curr[0]+1][curr[1]-1]==0: temp.append((curr[0]+1,curr[1]-1))
                if curr[1]+1<m and grid[curr[0]+1][curr[1]+1]==0: temp.append((curr[0]+1,curr[1]+1))
            if curr[1]-1>=0 and grid[curr[0]][curr[1]-1]==0: temp.append((curr[0],curr[1]-1))
            if curr[1]+1<m and grid[curr[0]][curr[1]+1]==0: temp.append((curr[0],curr[1]+1))
            
            for tup in temp:
                grid[tup[0]][tup[1]]=1
                queue.append((tup,num+1))
            
        return -1