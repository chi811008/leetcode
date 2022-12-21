import math

# class MedianFinder:

#     def __init__(self):
#         self.len_num = 0
#         self.nums = list()
        

#     def addNum(self, num: int) -> None:
#         self.nums.append(num)
#         self.len_num += 1
        

#     def findMedian(self) -> float:
#         self.nums.sort()
#         if self.len_num % 2 == 0:
#             ind1 = int(self.len_num / 2)
#             ind2 = ind1 - 1
#             median = sum(self.nums[ind2: ind1 + 1]) / 2
#         else:
#             ind = int(math.floor(self.len_num / 2))
#             median = self.nums[ind]
        
#         return median

import heapq

class MedianFinder:

    def __init__(self):
        self.left_nums = list()
        self.right_nums = list()
        heapq.heapify(self.left_nums)
        heapq.heapify(self.right_nums)
        

    def addNum(self, num: int) -> None:
        if self.right_nums and num > self.right_nums[0]:
            heapq.heappush(self.right_nums, num)
            ele = heapq.heappop(self.right_nums)
            heapq.heappush(self.left_nums, -ele)
        else:
            heapq.heappush(self.left_nums, -num)
        if len(self.left_nums) - len(self.right_nums) > 1:
            ele = heapq.heappop(self.left_nums)
            heapq.heappush(self.right_nums, -ele)
            
    def findMedian(self) -> float:
        if len(self.left_nums) > len(self.right_nums):
            return -self.left_nums[0]
            
        return (-self.left_nums[0] + self.right_nums[0]) / 2
    
m = MedianFinder()
m.addNum(1)
m.findMedian()
m.addNum(2)
m.findMedian()
m.addNum(3)
m.findMedian()