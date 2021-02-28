# https://leetcode.com/problems/maximum-frequency-stack/
class FreqStack:
    def __init__(self):
        self.df=defaultdict(list)
        self.pd=defaultdict(int)
        self.heap=[]
        heapq.heapify(self.heap)

    def push(self, x: int) -> None:
        self.pd[x]+=1
        self.df[self.pd[x]].append(x)
        if len(self.df[self.pd[x]])==1: heapq.heappush(self.heap,-self.pd[x])
            

    def pop(self) -> int:
        val = self.heap[0]
        new_val = self.df[-val].pop()
        self.pd[new_val]-=1
        if len(self.df[-val])==0: heapq.heappop(self.heap)
        return new_val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()