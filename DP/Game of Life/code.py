class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board[0])
        n=len(board)
        def neighbours(i,j):
            # print(i,j)
            count=0
            if i>0:
                count+=board[i-1][j]
                if j>0: count+=board[i-1][j-1]
                if j+1<m: count+=board[i-1][j+1]
            if i+1<n:
                count+=board[i+1][j]
                if j>0: count+=board[i+1][j-1]
                if j+1<m: count+=board[i+1][j+1]
            if j>0:
                count+=board[i][j-1]
            if j+1<m:
                count+=board[i][j+1]
            return count

        changes=[]
        for i in range(n):
            for j in range(m):
                count=neighbours(i,j)
                print(count)
                is_0=board[i][j]
                if count<2 or count>3:
                    is_0=0
                elif count==3:
                    is_0=1
                if is_0 != board[i][j]: changes.append((i,j,is_0))
        for i,j,val in changes:
            board[i][j]=val
        return
                