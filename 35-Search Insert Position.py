nums = [1,3,5,6, 7, 8, 9, 10, 11] # 9
target = 2

head, tail = 0, len(nums) - 1
while head <= tail:
    mid = (head + tail) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        tail = mid - 1
    else:
        head = mid + 1

return head