# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inn=defaultdict(set)
        out=defaultdict(set)
        for pair in prerequisites:
            inn[pair[0]].add(pair[1])
            out[pair[1]].add(pair[0])
        
        insidecount=defaultdict(int)
        for val in list(out):
            if len(inn[val])>0: continue
            stack=[(val,None)]
            while(len(stack)>0):
                curr=stack.pop()
                for var in out[curr[0]]:
                    if len(inn[var])==insidecount[var]+1:
                        stack.append([var,curr[0]])
                    insidecount[var]+=1

        for k,i in inn.items():
            if len(i)==0: continue
            elif len(i)!=insidecount[k]: return False
        return True
