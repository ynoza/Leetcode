# https://leetcode.com/problems/powerful-integers/
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        s=set()
        i=0
        j=0
        while x**i < bound:
            while x**i+y**j<=bound:
                s.add(x**i+y**j)
                j+=1
                if y==1: break
            j=0
            i+=1
            if x==1: break
        return list(s)