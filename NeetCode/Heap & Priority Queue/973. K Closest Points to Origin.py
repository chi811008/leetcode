import heapq
from collections import defaultdict 
import math
# class Solution:
#     def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
#         distance_points = defaultdict(list)
#         min_distance = list()
#         heapq.heapify(min_distance)
#         ans = list()
#         for x, y in points:
#             d = math.sqrt(x ** 2 + y ** 2)
#             distance_points[d].append([x, y])
#             heapq.heappush(min_distance, -d)
#             if len(min_distance) > k:
#                 heapq.heappop(min_distance)

#         min_distance = set(list(min_distance))
#         for d in min_distance:
#             for ele in distance_points[-d]:
#                 ans.append(ele)
#         return ans

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = list()
        for x, y in points:
            d = x ** 2 + y ** 2
            min_heap.append([d, x, y])
        heapq.heapify(min_heap)
        res = list()
        for i in range(k):
            d, x, y = min_heap[i]
            res.append([x, y])
        return res
            

    
s = Solution()
points = [[1,3],[-2,2]]
k = 1
ans = s.kClosest(points, k)
print(ans)