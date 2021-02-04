class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        start=True
        while (start or slow !=fast):
            start=False
            slow=nums[slow]
            fast=nums[nums[fast]]
            print(slow,fast)
        
        slow=nums[0]
        while(slow !=fast):
            slow=nums[slow]
            fast=nums[fast]
        return slow