# https://leetcode.com/problems/maximum-gap/
class Solution:
    def maximumGap(self, nums):
        n, minimum, maximum =len(nums), min(nums), max(nums)
        if n<3 or maximum==minimum: return abs(nums[0]-nums[-1])
        dic = defaultdict(list)
        for num in nums:
            if num==maximum:
                ind = n-2
            else:
                ind = (num-minimum)*(n-1) // (maximum - minimum)
            dic[ind].append(num)
        
        cands=[]
        maxSoFar=float('-inf')
        for i in range(n-1):
            if dic[i]:
                cands.append((min(dic[i]),max(dic[i])))
                if len(cands)>1:
                    maxSoFar=max(maxSoFar, cands[-1][0]-cands[-2][1])
        return maxSoFar