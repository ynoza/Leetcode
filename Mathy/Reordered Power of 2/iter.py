# https://leetcode.com/problems/reordered-power-of-2/
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        n=N
        d=[0]*10
        while(n>0):
            d[n%10]+=1
            n=n//10
        # print(d)
        start=1
        length=1
        val= math.floor(math.log10(N))+1
        while(length<=val):
            if length == val:
                temp_d=d.copy()
                temp_start=start
                while(temp_start>0):
                    temp_d[temp_start%10]-=1
                    if temp_d[temp_start%10]<0: break
                    temp_start=temp_start//10
                
                b=True
                for i in temp_d:
                    if i<0: 
                        b=False
                        break
                if b: return True
                
            start*=2
            length=math.floor(math.log10(start))+1
            # print(start,length)
        return False
        