# https://leetcode.com/problems/design-underground-system/
class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = Counter()
        # self.freqs = Counter()
        
    def checkIn(self, id, stationName, t):
        self.ids[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        Name2, t2 = self.ids[id]
        del self.ids[id]
        if (Name2, stationName) not in self.pairs:
            self.pairs[(Name2, stationName)]=[t-t2,1]  
        else:
            self.pairs[(Name2, stationName)][0]+= t-t2
            self.pairs[(Name2, stationName)][1]+= 1
        
    def getAverageTime(self, startStation, endStation):
        val=self.pairs[startStation, endStation]
        return val[0]/val[1]