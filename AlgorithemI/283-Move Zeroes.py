nums = [0,1,0,3,12]
slow_p = 0

for fast_p in range(len(nums)):
    if nums[fast_p] != 0:
        nums[slow_p], nums[fast_p] = nums[fast_p], nums[slow_p]
        slow_p += 1

print(nums)
