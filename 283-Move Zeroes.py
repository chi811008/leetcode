nums = [0,1,0,3,12]
slow_p = 0
quick_p = 0
nums_len = len(nums) # 5

while quick_p < nums_len:
    if nums[quick_p] != 0:
        nums[slow_p], nums[quick_p] = nums[quick_p], nums[slow_p]
        slow_p += 1
    quick_p += 1



print(nums)
















p = 0

for non_zero_p in range(len(nums)):
    if nums[non_zero_p] != 0:
        nums[p], nums[non_zero_p] = nums[non_zero_p], nums[p]
        p += 1
print(nums)
