# https://leetcode.com/problems/advantage-shuffle/
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        temp=B
        ret=[]
        B=sorted(B)
        A.sort()
        d=defaultdict(list)
        l=len(A)
        i=0
        while(i<l):
            if A[i]>B[i]:
                d[B[i]].append(A[i])
                i+=1
            else:
                A.append(A[i])
                A=A[:i]+A[i+1:]
                l-=1
        while (i<len(A)):
            d[B[i]].append(A[i])
            i+=1
        
        for b in temp:
            ret.append(d[b].pop())
        return ret