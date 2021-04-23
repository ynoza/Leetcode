# https://leetcode.com/problems/brick-wall/
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dp=defaultdict(int)
        dp[-1]=0
        for w in wall:
            s=w[0]
            for i in range(1,len(w)):
                dp[s]+=1
                s+=w[i]
        minSoFar = max(dp.values())
        return len(wall) - minSoFar