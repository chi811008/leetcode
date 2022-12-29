# from collections import defaultdict
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         s_method = defaultdict(int)
#         def s(n):
#             if n == 0:
#                 return 0
#             elif n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
            

#             s1 = s_method[n - 1] if n - 1 in s_method else s(n - 1)
#             s2 = s_method[n - 2] if n - 2 in s_method else s(n - 2)
#             method = s1 + s2
#             s_method[n] = method
            
#             return method
        
#         return s(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            method = one + two
            one, two = two, method
        return two
a = Solution().climbStairs(5)
print(a)