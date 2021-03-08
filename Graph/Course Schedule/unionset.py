# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites=sorted(prerequisites, key=lambda x: (x[1],x[0]))
        prerequisites=prerequisites + prerequisites[:3]
        inn=defaultdict(set)
        out=defaultdict(set)
        for pair in prerequisites:
            if pair[1] in out[pair[0]]: return False
            if pair[0] in inn[pair[1]]: return False
            inn[pair[0]].add(pair[1])
            inn[pair[0]]|= inn[pair[1]]
            out[pair[1]].add(pair[0])
            out[pair[1]]|= out[pair[0]]
        return True
