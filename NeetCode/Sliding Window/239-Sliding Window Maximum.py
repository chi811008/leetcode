nums = [1,3,-1,-3,5,3,6,7]
k = 3

ans = list()
max_num = [nums[0]]
for i in range(1, k):
    while max_num and (nums[i] > max_num[-1]):
        max_num.pop()
    max_num.append(nums[i])
ans.append(max_num[0])

for r in range(k, len(nums)):
    while max_num and (nums[r] > max_num[-1]):
        max_num.pop()
    max_num.append(nums[r])

    if nums[r - k] == max_num[0]:
        max_num.pop(0)
    ans.append(max_num[0])
print(ans)