nums = [-1,0,3,5,9,12]
target = 13
def bs(head, tail):
    if head > tail:
        return -1
    mid = (head + tail) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bs(mid + 1, tail)
    else:
        return bs(head, mid - 1)

head, tail = 0, len(nums) - 1
while head <= tail:
    mid = (head + tail) // 2
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        head = mid + 1
    else:
        tail = mid - 1
print(-1)