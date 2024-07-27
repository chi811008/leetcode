nums = [2,7,11,15]
target = 9
num_map = dict()
for i in range(len(nums)):
    ans = num_map.get(target - nums[i])
    if ans is not None:
        print([ans, i])
    num_map[nums[i]] = i
















# imap = dict()
# for i, value in enumerate(nums):
#     if value in imap:
#         print(imap[value], i)
#     imap[target - value] = i