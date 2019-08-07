from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        table = defaultdict(lambda _: [False] * numCourses)
        for course, pre in prerequisites:
            table[course][pre] = True

        

        