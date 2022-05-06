nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = 6
curr = res = nums[0]
for i in range(1, len(nums)):
    curr += nums[i]
    if nums[i] > curr:
        curr = nums[i]
    if curr > res:
        res = curr
print(res)

# O(n2) bruce
nums = [-1,0,-2]
max_sum = nums[0]
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total > max_sum:
            max_sum = total
print(max_sum)