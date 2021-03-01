# https://leetcode.com/problems/distribute-candies/
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d=set()
        count=0
        n=len(candyType)
        prev=None
        for i in candyType:
            if i!=prev and i not in d: 
                d.add(i)
                count+=1
                if count==n/2:
                    break
            else: prev=i
        return count