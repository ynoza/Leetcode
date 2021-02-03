class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur (arr, sofar, ret):
            if len(arr)==0:
                return
            elif len(arr)==1:
                x.append(sofar+arr)
                return
            for i in range(len(arr)):
                recur(arr[:i]+arr[i+1:],sofar+[arr[i]], x)
        x=[]
        recur(nums,[],x)
        return x    