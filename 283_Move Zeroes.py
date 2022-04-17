nums = [0,1,0,3,12]
p = 0
for non_zero_p in range(len(nums)):
    if nums[non_zero_p] != 0:
        nums[p], nums[non_zero_p] = nums[non_zero_p], nums[p]
        p += 1
print(nums)
