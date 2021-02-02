def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binsearch(left,right,bias,tag):
            mid=int((left+right)/2)
            # print(nums[mid])
            # if bias==0:print(left,mid,right,nums[mid],bias)
            if left>right:
                return -1
            elif nums[left]==tag and bias==0:
                return left
            elif nums[right]==tag and bias==1:
                return right
            # elif nums[mid] == tag:
            #     return mid
            elif nums[mid]<tag:
                return binsearch(mid+1,right,bias,tag)
            elif nums[mid]>tag:
                return binsearch(left,mid-1,bias,tag)
            elif bias==0:
                return binsearch(left+1,mid,bias,tag)
            else:
                return binsearch(mid,right-1,bias,tag)
                
                
        n=len(nums)-1
        left=binsearch(0,n,0,target)
        right=binsearch(0,n,1,target)