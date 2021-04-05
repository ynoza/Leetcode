# https://leetcode.com/problems/global-and-local-inversions/
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i,a in enumerate(A):
            if a==i or i+1==a or i-1==a: continue
            else: return False
        return True