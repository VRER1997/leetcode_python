import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegree = [0]*numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        return self.topologicalSort(graph, indegree) == numCourses

    def topologicalSort(self, graph, indegree):
        count = 0
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop()
            count += 1
            for i in graph[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return count