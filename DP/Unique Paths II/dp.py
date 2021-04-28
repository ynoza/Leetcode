# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1: return 0
        obstacleGrid[0][0]=-1
        for i in range(m):
            for j in range(n):
                val1=0
                val2=0
                if i-1>=0 and obstacleGrid[i-1][j]<1:
                    val1=obstacleGrid[i-1][j]
                if j-1>=0 and obstacleGrid[i][j-1]<1:
                    val2=obstacleGrid[i][j-1]
                if obstacleGrid[i][j]<1:
                    obstacleGrid[i][j]+=val1+val2
        # print(obstacleGrid)
        return -obstacleGrid[m-1][n-1]