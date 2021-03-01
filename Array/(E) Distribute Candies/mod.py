# https://leetcode.com/problems/distribute-candies/
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        d=set(candyType)
        return int(min(n/2,len(d)))