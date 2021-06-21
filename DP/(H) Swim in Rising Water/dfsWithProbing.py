# https://leetcode.com/problems/swim-in-rising-water/
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        stack=[(0,0)]
        dic={}
        maxVal=grid[0][0]
        grid[0][0]=float('inf')
        while(len(stack)>0 or len(dic.keys())>0):
            if len(stack)>0:
                i,j=stack.pop()
                if i==len(grid)-1 and j==len(grid[0])-1:
                    return maxVal
                if i-1>=0:
                    if grid[i-1][j]<=maxVal:
                        stack.append((i-1,j))
                    elif grid[i-1][j]!=float('inf'):
                        dic[grid[i-1][j]]=(i-1,j)
                    grid[i-1][j]=float('inf')
                if i+1<len(grid):
                    if grid[i+1][j]<=maxVal:
                        stack.append((i+1,j))
                    elif grid[i+1][j]!=float('inf'):
                        dic[grid[i+1][j]]=(i+1,j)
                    grid[i+1][j]=float('inf')
                if j-1>=0:
                    if grid[i][j-1]<=maxVal:
                        stack.append((i,j-1))
                    elif grid[i][j-1]!=float('inf'):
                        dic[grid[i][j-1]]=(i,j-1)
                    grid[i][j-1]=float('inf')
                if j+1<len(grid[0]):
                    if grid[i][j+1]<=maxVal:
                        stack.append((i,j+1))
                    elif grid[i][j+1]!=float('inf'):
                        dic[grid[i][j+1]]=(i,j+1)
                    grid[i][j+1]=float('inf')
            else:
                while(maxVal not in dic):
                    maxVal+=1
                stack.append(dic[maxVal])
                del dic[maxVal]
        return -1