nums = [7,7,7,7,7,7,7]

# O(n^2)
nums_len = len(nums)
max_length = [1] * nums_len
ans = 1
for i in range(nums_len - 2, -1, -1):
    _max_length = max_length[i]
    for j in range(i + 1, nums_len):
        if nums[i] < nums[j]:
            _length = max_length[i] + max_length[j]
            if _length > _max_length:
                _max_length = _length
    max_length[i] = _max_length
    if _max_length > ans:
        ans = _max_length
print(ans)
                
        