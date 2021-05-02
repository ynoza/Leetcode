# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
        lst=[0,0,0]
        for i in range(len(nums)):
            temp=nums[i]
            swap(lst[nums[i]],i)
            if i>0 and nums[i]<nums[i-1]: swap(lst[nums[i]],i)
            for j in range(temp,3):
                lst[j]+=1
            
            
            lst[1]=max(lst[0],lst[1])
            lst[2]=max(lst[0],lst[1],lst[2])
