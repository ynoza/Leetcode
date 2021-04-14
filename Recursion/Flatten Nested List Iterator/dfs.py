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
        self.lst=[]
        self.nested=nestedList
        # self.dfs(nestedList)
    
    def dfs(self, lst):
        for l in lst:
            if l.isInteger(): self.lst.append(l.getInteger())
            else: self.dfs(l.getList())
        
                
    def next(self) -> int:
        # print(self.lst)
        if len(self.lst)>0: 
            return self.lst.pop(0)
        elif self.nested[0].isInteger():
            # print(self.nested[0])
            return self.nested.pop(0).getInteger()
        else:
            self.dfs(self.nested.pop(0).getList())
            return self.next()
            
        
    def hasNext(self) -> bool:
         return len(self.lst)>0 or len(self.nested)>0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())