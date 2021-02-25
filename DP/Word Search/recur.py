# https://leetcode.com/problems/word-search/
class Solution:   
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word)==0: return True
        m=len(board)
        n=len(board[0])
        # print(m,n)
        ans=[False]
        def dfs(k,l,ind):
            if ind==len(word):
                ans[-1]=True
                return
            if (k+1<m and board[k+1][l]==word[ind]):
                board[k+1][l]=0
                dfs(k+1,l,ind+1)
                if ans[-1]: return True
                board[k+1][l]=word[ind]
            if (k-1>=0 and board[k-1][l]==word[ind]): 
                board[k-1][l]=0
                dfs(k-1,l,ind+1)
                if ans[-1]: return True
                board[k-1][l]=word[ind]
            if (l+1<n and board[k][l+1]==word[ind]):
                board[k][l+1]=0
                dfs(k,l+1,ind+1)
                if ans[-1]: return True
                board[k][l+1]=word[ind]
            if (l-1>=0 and board[k][l-1]==word[ind]):
                board[k][l-1]=0
                dfs(k,l-1,ind+1)
                if ans[-1]: return True
                board[k][l-1]=word[ind]
                
        for i in range(m):
            for j in range(n):
                if (word[0]==board[i][j]):
                    board[i][j]=0
                    dfs(i,j,1)
                    if ans[-1]: return True
                    board[i][j]=word[0]
        return False
                        