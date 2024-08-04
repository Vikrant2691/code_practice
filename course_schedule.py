from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         
         courses = dict()
         for i in prerequisites:
             c,p = i
             if c not in courses:
                 courses[c] = set()
             courses[c].add(p)
         
         count = set()
         
         