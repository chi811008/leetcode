nums = [1,2,3]
k = 4

if k == 0:
    pass
else:
    nums_len = len(nums)
    p_head = 0
    residual = nums_len % k
    if residual == 0:
        for i in range(nums_len // k):
            p_tail = -k
            for j in range(k):
                nums[p_head], nums[p_tail] = nums[p_tail], nums[p_head]
                p_head += 1
                p_tail += 1
    else:
        for i in range(nums_len // k):
            p_tail = -k
            for j in range(k):
                nums[p_head], nums[p_tail] = nums[p_tail], nums[p_head]
                p_head += 1
                p_tail += 1
        for k in range(residual - 1):
            nums[p_head], nums[p_head + 1] = nums[p_head + 1], nums[p_head]
            p_head += 1




print(nums)