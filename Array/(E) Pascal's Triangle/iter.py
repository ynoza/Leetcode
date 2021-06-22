# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        start=[[1]]
        for i in range(1,numRows):
            newLst=[1]
            j=0
            for i in range(1,i):
                newLst.append(start[-1][j]+start[-1][j+1])
                j+=1
            newLst.append(1)
            start.append(newLst)
        return start
    