from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_to_pre = defaultdict(list)
        for course, pre in prerequisites:
            course_to_pre[course].append(pre)
        
        visited = set()
        def dfs(course):
            if course not in course_to_pre:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for pre in course_to_pre.pop(course):
                if not dfs(pre):
                    return False
            visited.remove(course)
            return True
        
        for k in course_to_pre.keys():
            if not dfs(k):
                return False
        return True
            