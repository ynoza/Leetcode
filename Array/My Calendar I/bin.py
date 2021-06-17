# https://leetcode.com/problems/my-calendar-i/
class MyCalendar:

    def __init__(self):
        self.lst=[]
        

    def book(self, start: int, end: int) -> bool:
        if len(self.lst)==0:
            self.lst.append((start,end))
            return True
        elif self.lst[0][0]>=end:
            self.lst=[(start,end)]+self.lst
            return True
        elif self.lst[-1][1]<=start:
            self.lst.append((start,end))
            return True
        # print(self.lst)
        l,r=0,len(self.lst)-1
        while(l<=r):
            mid=(l+r)//2
            # print(mid)
            if mid>0 and self.lst[mid-1][1]<= start and self.lst[mid][0]>=end:
                self.lst=self.lst[:mid] + [(start,end)]+ self.lst[mid:]
                return True
            elif self.lst[mid][0]<=start and start<self.lst[mid][1]: return False
            elif self.lst[mid][0]<end and end<=self.lst[mid][1]: return False
            elif self.lst[mid][0]==start: return False
            elif self.lst[mid][0]<start:
                l=mid+1
            else:
                r=mid-1
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)