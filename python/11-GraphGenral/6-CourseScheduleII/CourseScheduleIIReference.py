class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        visited, cycle = set(), set()
        graph = defaultdict(list)
        
        for (u,v) in prerequisites:
            graph[u].append(v)
        
        def dfs(course):
            if course in visited:
                return False

            if course in cycle:
                return True

            visited.add(course)
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            ret.append(course)
            cycle.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return ret