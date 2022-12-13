# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[len(nums) - k]

# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         max_heap = [-num for num in nums]
#         heapq.heapify(max_heap)
        
#         for i in range(k):
#             res = heapq.heappop(max_heap)
#         return -res

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k 
        def quick_sort(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p < k:
                return quick_sort(p + 1, r)
            elif p > k:
                return quick_sort(l, p - 1)
            else:
                return nums[k]
        res = quick_sort(0, len(nums) - 1)
        return res
        

nums = [3,2,3,1,2,4,5,5,6]
k = 4
ans = Solution().findKthLargest(nums, k)
print(ans)
