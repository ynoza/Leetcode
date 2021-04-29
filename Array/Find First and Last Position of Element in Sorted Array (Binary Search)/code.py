# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def biniterleft(target):
            nonlocal nums
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=(l+r)//2
                if mid==0 and nums[mid]==target: return mid
                elif mid>0 and nums[mid]==target and nums[mid-1]<target: return mid
                elif nums[mid]>=target: r=mid-1
                else: l=mid+1
            return -1
        def biniterright(target):
            nonlocal nums
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=(l+r)//2
                if mid==len(nums)-1 and nums[mid]==target: return mid
                elif mid<len(nums)-1 and nums[mid]==target and nums[mid+1]>target: return mid
                elif nums[mid]<=target: l=mid+1
                else: r=mid-1
            return -1
        return [biniterleft(target),biniterright(target)]
        