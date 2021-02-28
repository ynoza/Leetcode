# https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1: return 2147483647
        mult1=1
        mult2=1
        if dividend<0:
            mult1=-1
            dividend=-dividend
        if divisor<0:
            mult2=-1
            divisor=-divisor
            
        if dividend<divisor: return 0
        
        i=1
        val=divisor
        while(val<=dividend):
            i+=i
            val+=val

        # print(i,val,dividend)
        ret=0
        while(val>=divisor):
            if dividend>=val:
                dividend-=val
                ret+=i
            i>>=1
            val>>=1
        
        # print(i,val,dividend)
        return ret*mult1*mult2
        