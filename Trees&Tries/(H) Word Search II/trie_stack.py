# https://leetcode.com/problems/word-search-ii/
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d={}
        speed_up={}
        for word in words:
            if word[0] in speed_up:
                speed_up[word[0]].add(word)
            else:
                speed_up[word[0]]=set()
                speed_up[word[0]].add(word)
            i=0
            at=d
            while(i<len(word) and word[i] in at):
                at=at[word[i]]
                i+=1
            while(i<len(word)):
                at[word[i]]={}
                at=at[word[i]]
                i+=1
            at[len(word)]=word
        # print(d)
        
        ret=set()
        m=len(board)
        n=len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(ret)==len(words): return list(ret)
                elif board[i][j] in d and len(speed_up[board[i][j]])>0:
                    visited=set()
                    visited.add((i,j))
                    stack=[(i,j,1,d[board[i][j]], visited)]
                    while(len(stack)>0 and len(speed_up[board[i][j]])>0):
                        k,l,at,dic,vis=stack.pop()
                        # print(k,l,at,dic)
                        if at in dic: 
                            # print(vis)
                            if dic[at] in speed_up[dic[at][0]]: speed_up[dic[at][0]].remove(dic[at])
                            ret.add(dic[at])

                        if k+1<m and (k+1,l) not in vis and board[k+1][l] in dic:
                            temp=vis.copy()
                            temp.add((k+1,l))
                            stack.append([k+1,l,at+1,dic[board[k+1][l]],temp])

                        if k-1>=0 and (k-1,l) not in vis and board[k-1][l] in dic:
                            temp=vis.copy()
                            temp.add((k-1,l))
                            stack.append([k-1,l,at+1,dic[board[k-1][l]],temp])

                        if l-1>=0 and (k,l-1) not in vis and board[k][l-1] in dic:
                            temp=vis.copy()
                            temp.add((k,l-1))
                            stack.append([k,l-1,at+1,dic[board[k][l-1]],temp])

                        if l+1<n and (k,l+1) not in vis and board[k][l+1] in dic:
                            temp=vis.copy()
                            temp.add((k,l+1))
                            stack.append([k,l+1,at+1,dic[board[k][l+1]],temp])
        return list(ret)
                