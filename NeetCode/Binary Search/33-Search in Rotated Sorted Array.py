nums = [5,1,2,3,4]
target = 6

def bs(head, tail):
    while head <= tail:
        mid = (head + tail) // 2
        if nums[mid] == target:
            return mid
        elif nums[head] <= nums[mid]:
            if target < nums[head] or target > nums[mid]:
                head = mid + 1
            else:
                tail = mid - 1
        else:
            if target > nums[tail] or target < nums[mid]:
                tail = mid - 1
            else:
                head = mid + 1
    return -1
ans = bs(0, len(nums) - 1)
print(ans)
            





# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def find_end_num(head, tail):
#             if nums[tail] >= nums[head]:
#                 return tail
#             while head <= tail:
#                 mid = (head + tail) // 2
#                 if nums[mid] > nums[mid + 1]:
#                     return mid
#                 elif nums[head] <= nums[mid] <= nums[tail]:
#                     head = mid + 1
#                 elif nums[mid] >= nums[tail] and nums[mid] >= nums[head]:
#                     head = mid + 1
#                 elif nums[mid] <= nums[head] and nums[mid] <= nums[tail]:
#                     tail = mid - 1

#         def bs(head, tail):
#             while head <= tail:
#                 mid = (head + tail) // 2
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] < target:
#                     head = mid + 1
#                 elif nums[mid] > target:
#                     tail = mid - 1
#             return -1

#         end_num = find_end_num(0, len(nums) - 1)

#         if nums[0] <= target <= nums[end_num] or end_num == len(nums) - 1:
#             ans = bs(0, end_num)
#         elif nums[end_num + 1] <= target <= nums[-1]:
#             ans = bs(end_num + 1, len(nums) - 1)
#         else:
#             ans = -1
#         return ans

