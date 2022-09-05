nums = [3,1, 2]
min_num = nums[0]
head, tail = 0, len(nums) - 1
while head <= tail:
    if nums[head] < nums[tail]:
        min_num = (min(min_num, nums[head]))
        break
    
    mid = (head + tail) // 2
    min_num = min(min_num, nums[mid])
    if nums[mid] >= nums[head]:
        # search right
        head = mid + 1
    else:
        # search left
        tail = mid - 1
print(min_num)

# def find_min(head, tail, min_num):
#     if len(nums) == 1:
#         return min_num
#     while head <= tail:
#         mid = (head + tail) // 2
#         min_num = min(min_num, nums[mid])
#         if nums[head] <= nums[mid]:
#             if nums[tail] < nums[head]:
#                 head = mid + 1
#             else:
#                 tail = mid - 1
#         else:
#             tail = mid - 1
#     return min_num
# ans = find_min(0, len(nums) - 1, min_num)
# print(ans)

# def find_end_num(head, tail):
#     if nums[tail] >= nums[head]:
#         return tail
#     while head <= tail:
#         mid = (head + tail) // 2
#         if nums[mid] > nums[mid + 1]:
#             return mid
#         elif nums[head] <= nums[mid] <= nums[tail]:
#             head = mid + 1
#         elif nums[mid] >= nums[tail] and nums[mid] >= nums[head]:
#             head = mid + 1
#         elif nums[mid] <= nums[head] and nums[mid] <= nums[tail]:
#             tail = mid - 1
# end_num = find_end_num(0, len(nums) - 1)
# print(end_num)