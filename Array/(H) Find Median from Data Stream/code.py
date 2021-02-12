# https://leetcode.com/problems/find-median-from-data-stream/submissions/
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small=[]
        self.large=[]
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        
        if len(self.small)==0:
            heapq.heappush(self.small,num)
        elif len(self.large)< len(self.small):
            if num> self.small[0]:
                temp=heapq.heappop(self.small)
                heapq.heappush(self.small,num)
                heapq.heappush(self.large,-1*temp)
            else:
                heapq.heappush(self.large,-1*num)
        else:
            if num>=-1*self.large[0]:
                heapq.heappush(self.small,num)
            else:
                temp=heapq.heappop(self.large)
                heapq.heappush(self.large,-1*num)
                heapq.heappush(self.small,-1*temp)
                
            
    def findMedian(self) -> float:
        # print(self.small,self.large)
        if len(self.small)>len(self.large):
            return self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]*-1
        return (self.small[0]+(-1)*self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()