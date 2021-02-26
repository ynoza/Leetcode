# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        def recur(at,path,x):
            if at==n-1:
                x.append(path+[n-1])
                return
            temp=path+[at]
            for i in graph[at]:
                recur(i,temp,x)
        x=[]
        recur(0,[],x)
        return x
            