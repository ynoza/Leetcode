# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
class Solution:
    def minPartitions(self, n: str) -> int:
        # maxSoFar=0
        # for num in n:
        #     if int(num)>maxSoFar: maxSoFar=int(num)
        # print(max(n))
        # return maxSoFar
        return max(n)