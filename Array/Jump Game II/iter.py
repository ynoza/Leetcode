# https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        start=1
        end=nums[0]
        count=1
        while(end<len(nums)-1):
            temp=(float('-inf'),-1)
            for i in range(start,end+1):
                if nums[i]-(end-i)>temp[0]:
                    temp=(nums[i]-(end-i),i)
            start=temp[1]+1
            end=temp[1]+nums[temp[1]]
            count+=1
            # if count==10: return count
            # print(start,end,count)
        return count