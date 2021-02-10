class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret=[]
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        for i in range(len(intervals)):
            if not ret or ret[-1][1]<intervals[i][0]:
                ret.append(intervals[i])
            else:
                ret[-1][1]=max(ret[-1][1],intervals[i][1])
        return ret