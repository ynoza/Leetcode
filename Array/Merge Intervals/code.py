class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret=[]
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if prev[0]<intervals[i][0] and prev[1]>intervals[i][1]: 
                continue
            elif intervals[i][0]<=prev[1] and intervals[i][1]>prev[1]:         
                prev=[prev[0],intervals[i][1]]
            elif intervals[i][0]> prev[1]:
                # print(intervals[i])
                ret.append(prev)
                prev=intervals[i]
        if prev: ret.append(prev)
        return ret