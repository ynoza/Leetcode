# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s1,s2=[0,cardPoints[0]],[]
        for i in range(1,k):
            s1.append(cardPoints[i]+s1[-1])

        maxVal=s1.pop()
        s2=0
        for i in range(len(cardPoints)-1,len(cardPoints)-1-k,-1):
            s2+=cardPoints[i]
            val=s1.pop()+s2
            if val>maxVal: maxVal=val
        
        return maxVal
        
        