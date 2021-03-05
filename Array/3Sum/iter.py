# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        cunt = Counter(nums)
        s = set(nums)
        if cunt[0]>=3:
            ret.append([0,0,0])
        
        pos=[]
        neg=[]
        for i in cunt.keys():
            if i < 0: neg.append(i)
            else: pos.append(i)
        
        for i in pos:
            for j in neg:
                val=-i-j
                if val not in cunt: continue
                temp=cunt[val]
                if temp==1 and i> val > j: ret.append([j,val,i])
                elif temp==2 and (i>= val > j or i> val >=j): ret.append([j,val,i])
                elif temp>=3 and (i>=val >=j or i>=val>=j): ret.append([j,val,i])
        
        return ret