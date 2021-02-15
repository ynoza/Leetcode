#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst=[]
        for i in range (len(mat)):
            sumsofar=0
            for n in mat[i]:
                if n: sumsofar+=1
                else: break
            lst.append((sumsofar,i))
        
        heapq.heapify(lst)
        return [heapq.heappop(lst)[1] for _ in range(k)]