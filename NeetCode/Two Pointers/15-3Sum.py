nums = [-1,0,1,2,-1,-4]
nums.sort()
print(nums)
nums_len = len(nums)
ans = list()
for i in range(nums_len):
    if i >= 1:
        if nums[i] == nums[i - 1]:
            continue
    find_sum = 0 - nums[i]
    head, tail = i + 1, nums_len - 1 
    while head < tail:
        if nums[head] + nums[tail] == find_sum:
            ans.append([nums[i], nums[head], nums[tail]])
            head += 1
            tail -+ 1
            while head < tail:
                print(head)
                if nums[head] == nums[head - 1]:
                    print(nums[head], nums[head - 1])
                    head += 1
                else:
                    break
        elif nums[head] + nums[tail] > find_sum:
            tail -= 1
        else:
            head += 1
print(ans)
