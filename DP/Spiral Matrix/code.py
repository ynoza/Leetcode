# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=0
        u=0
        m=len(matrix)
        n=len(matrix[0])
        if m==0:
            return []
        elif n==1:
            ret=[]
            for i in range(len(matrix)):
                ret.append(matrix[i][0])
            return ret
        d=m-1
        r=n-1
        end=m*n
        i,j=0,0
        ret=[matrix[i][j]]
        count=1
        while(j+1<=r):
            # print("hi")
            while(j+1<=r):
                j+=1
                ret.append(matrix[i][j])
                count+=1
            if count==m*n: break
            u+=1
            while(i+1<=d):
                i+=1
                ret.append(matrix[i][j])
                count+=1
            if count==m*n: break
            r-=1
            while(j-1>=l):
                j-=1
                ret.append(matrix[i][j])
                count+=1
            if count==m*n: break
            d-=1
            while(i-1>=u):
                i-=1
                ret.append(matrix[i][j])
                count+=1
            if count==m*n: break
            l+=1
        return ret
