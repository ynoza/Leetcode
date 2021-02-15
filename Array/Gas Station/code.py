#https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        s=[]
        rs=[]
        maxs=(-1,-1)
        for i in range(len(gas)):
            if i==0: 
                s.append(gas[i]-cost[i])
                rs.append(gas[len(gas)-1-i]-cost[len(gas)-1-i])
            else: 
                s.append(gas[i]-cost[i]+s[i-1])
                rs.append(gas[len(gas)-1-i]-cost[len(gas)-1-i]+rs[i-1])
            if rs[i]>=maxs[0]: maxs=(rs[i],len(gas)-1-i)
        
        if s[-1]<0: return -1
        return maxs[1]