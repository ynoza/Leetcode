class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height=len(matrix)
        for h in range(math.ceil(height/2)):
            for i in range(h,height-h-1):
                # print((h,i), (height-i-1,h))
                # print((height-h-1,height-i-1), (i,height-h-1))
                temp=matrix[h][i]
                matrix[h][i] = matrix[height-i-1][h]
                matrix[height-i-1][h] = matrix[height-h-1][height-i-1]
                matrix[height-h-1][height-i-1] = matrix[i][height-h-1]
                matrix[i][height-h-1] = temp