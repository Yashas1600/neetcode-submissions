class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        preMap = defaultdict(list)
        for pre in prerequisites:
                preMap[pre[0]].append(pre[1])
        
        result = []
        visited = {} #0 = unvisited, 1 = visiting, 2 = visited

        def dfs(course):
            if course in visited:
                if visited[course] == 1:
                    return False
                else:
                    return True
            visited[course] =1

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited[course] = 2
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result