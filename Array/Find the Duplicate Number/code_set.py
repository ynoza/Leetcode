class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited=set()
        for n in nums:
            if n in visited: return n
            else: visited.add(n)
        return None