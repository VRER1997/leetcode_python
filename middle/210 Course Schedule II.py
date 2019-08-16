from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for i in range(numCourses)]
        edges = [[] for i in range(numCourses)]

        for front, tail in prerequisites:
            indegrees[front] += 1
            edges[tail].append(front)

        courses = set(range(numCourses))
        flag = True
        order = []

        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if indegrees[x] == 0:
                    for node in edges[x]:
                        indegrees[node] -= 1
                    removeList.append(x)
                    order.append(x)
                    flag = True
            for x in removeList:
                courses.remove(x)

        return order if len(courses) == 0 else []