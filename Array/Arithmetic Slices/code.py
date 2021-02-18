# https://leetcode.com/problems/arithmetic-slices/
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<3: return 0
        diff=None
        ret=0
        count=1
        for i in range(1,len(A)):
            if diff!=A[i]-A[i-1]: 
                count=2
                diff=A[i]-A[i-1]
            else:
                count+=1
                if count >=3: ret+=(count-3)+1
            # print(count,ret)
        return ret