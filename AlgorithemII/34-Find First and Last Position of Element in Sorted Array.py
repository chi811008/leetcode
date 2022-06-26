nums = [5,7,7,8,8,10]
target = 1
# recursive binary search:
def bs(head, tail, nums, target):
    if head > tail:
        return -1
    mid = (head + tail) // 2 
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return bs(head + 1, mid - 1, nums, target)
    else:
        return bs(mid + 1, tail - 1, nums, target)
ans = bs(0, len(nums) - 1, nums, target)
print(ans)








ans = list()
for i in range(len(nums)):
    if nums[i] == target:
        ans.append(i)
        break

if len(ans) == 1:
    while i < len(nums) and (nums[i] == target):
        i += 1
    ans.append(i - 1)
else:
    print([-1, -1])

# binary search
_ = list()
head, tail = 0, len(nums) - 1
while head <= tail:
    mid = (head + tail) // 2
    if nums[mid] == target:
        _.append(mid)
        break
    elif nums[mid] < target:
        head = mid + 1
    else:
        tail = mid - 1
if len(_) == 0:
    print([-1, -1])
p_h = p_t = mid
while p_h > -1 and (nums[p_h] == target):
    p_h -= 1
while p_t < len(nums) and (nums[p_t] == target):
    p_t += 1
print([p_h + 1, p_t - 1])