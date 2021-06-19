# https://leetcode.com/problems/maximum-units-on-a-truck/Maximum Units on a Truck
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes, key=lambda x: x[1],reverse=True)
        boxTotal=0
        sumTotal=0
        # print(boxTypes)
        for i, lst in enumerate(boxTypes):
            a,b=lst
            if truckSize==boxTotal: return sumTotal
            tempVal=(truckSize-boxTotal)
            if a <= tempVal:
                boxTotal+=a
                sumTotal+=a*b
            else:
                boxTotal+=tempVal
                sumTotal+=tempVal*b
            # print(boxTotal, sumTotal)
        return sumTotal