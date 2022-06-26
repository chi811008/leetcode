nums = [1,5,11,5]
nums_sum = sum(nums)
if nums_sum % 2 != 0:
    return False

target = int(nums_sum / 2)
dp = set()
dp.add(0)
for i in range(len(nums)):
    if nums[i] == target:
        return True
    _dp = set()
    for t in dp:
        _ = nums[i] + t
        if _ == target:
            return True
        _dp.add(nums[i])
        _dp.add(_)
    dp = dp.union(_dp)
return True if target in dp else False