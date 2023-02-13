class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
    
        course_pres = {i:list() for i in range(numCourses)}
        for course, prerepuiste in prerequisites:
            course_pres[course].append(prerepuiste)

        # a course has three possible states:
        # visited -> course has been added to result
        # visiting -> course not in result but was added to cycle
        # unvisited -> course not added to result or cycle

        res = list()
        visited, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            elif course in visited:
                return True

            cycle.add(course)
            for pre in course_pres[course]:
                if not dfs(pre):
                    return False
            visited.add(course)
            res.append(course)
            cycle.remove(course)
            return True
            
        for k in course_pres.keys():
            if not dfs(k):
                return []
        return res

numCourses = 2
# prerequisites = [[1,3],[0,1],[0,2],[5,0],[4,0],[3,2]]
prerequisites = []
s = Solution().findOrder(numCourses, prerequisites)
res = [2, 3, 1, 0, 4, 5]
print(s)