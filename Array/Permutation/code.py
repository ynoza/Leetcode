class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(arr):
            if len(arr)==0:
                return []
            elif len(arr)==1:
                return arr
            sum=[]
            for i in range(len(arr)):
                # temp=[]
                for j in recur(arr[:i]+arr[i+1:]):
                    sum.append([arr[i]]+[j])
                # sum.append(temp)
            return sum
        ans = recur(nums)
        ret=[]
        for a in ans:
            temp=[]
            for i in range(0,len(nums)-1):
                temp.append(a[0])
                a=a[1]
            temp.append(a)
            ret.append(temp)
        # print(ans)
        # print(ret)
        return ret