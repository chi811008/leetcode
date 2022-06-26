nums = [-1,1,0,-3,3]
output = [0,0,9,0,0]
nums_len = len(nums)
ans = [1] * nums_len
pre_multiple, post_multiple = 1, 1
for i in range(nums_len):
	ans[i] = pre_multiple
	pre_multiple *= nums[i]

for i in range(nums_len - 1, -1, -1):
	ans[i] *= post_multiple
	post_multiple *= nums[i]
print(ans)

