nums = [-1]
k = 2
nums_len = len(nums)
ans = list()
for i in range(nums_len):
    ans.append(nums[-(k % nums_len) + i])
    print(-(k % nums_len) + i)
for i in range(nums_len):
    nums[i] = ans[i]
print(nums)