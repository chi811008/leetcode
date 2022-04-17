nums = [-7,-3,2,3,11]
len_nums = len(nums)
ans = [0] * len_nums
head, tail = 0, len_nums - 1
ans_index = tail
while head <= tail:
    if abs(nums[head]) > abs(nums[tail]):
        ans[ans_index] = nums[head] ** 2
        head += 1
    else:
        ans[ans_index] = nums[tail] ** 2
        tail -= 1
    ans_index -= 1
print(ans)









head, tail = 0, len(nums) - 1
ans = [0] * len(nums)
ans_index = tail
while head <= tail:
    if nums[head] ** 2 > nums[tail] ** 2:
        ans[ans_index] = nums[head] ** 2
        head += 1
    else:
        ans[ans_index] = nums[tail] ** 2
        tail -= 1
    ans_index -= 1
print(ans)