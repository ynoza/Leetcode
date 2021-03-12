# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ret=set()
        for i in range (len(s)-k+1):
            ret.add(s[i:i+k])
            
        return len(ret)==1<<k