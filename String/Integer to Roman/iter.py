# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        rom=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        
        ret=""
        i=0
        while(rom[i][0]>num): 
            i+=1
            
        while(num>0):
            val = rom[i][1]*(num//rom[i][0])
            ret+=val
            num%=rom[i][0]
            i+=1
        
        return ret