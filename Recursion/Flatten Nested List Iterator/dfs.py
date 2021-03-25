# https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList=nestedList
        self.segment=[]
    
    def solveNested(self,lst):
        for x in lst:
            if x.isInteger(): self.segment.append(x)
            else: self.solveNested(x.getList())
    
    def next(self) -> int:
        if len(self.segment)>0: 
            temp=self.segment.pop(0)
            return temp
        temp=self.nestedList.pop(0)
        if temp.isInteger(): return temp
        self.solveNested(temp.getList())
        return self.segment.pop(0)
    
    def hasNext(self) -> bool:
        if len(self.segment)>0: return True
        elif(len(self.nestedList)>0 and not self.nestedList[0].isInteger() and len(self.nestedList[0].getList())<=1):
            temp=self.nestedList.pop(0)
            self.solveNested(temp.getList())
            return self.hasNext()
        return len(self.nestedList)>0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())