# https://leetcode.com/problems/binary-trees-with-factors/
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        d=defaultdict(int)
        arr=sorted(arr)
        ret=0
        for i in range(len(arr)):
            d[arr[i]]+=1
            for j in range(i):
                val=arr[i]/arr[j]
                if val in d:
                    d[arr[i]]+=d[arr[j]]*d[val]
            ret+=d[arr[i]]
                
        return ret % (10**9+7)