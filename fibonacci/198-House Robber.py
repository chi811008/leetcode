house = [2,7,9,3,1]
rob1 = rob2 = 0
for i in range(len(house)):
    rob = max(rob2, house[i] + rob1)
    rob1, rob2 = rob2, rob
print(rob2)














# house = [0] * len(nums)
# house[-1], house[-2] = nums[-1], nums[-2]
# max_rob = max(house[-1], house[-2])
# for i in range(len(nums) - 3, -1, -1):
#     _max = nums[i]
#     for j in range(i + 2, len(nums)):
#         if (nums[i] + house[j]) > _max:
#             _max = nums[i] + house[j]
#     house[i] = _max
#     print(_max)
#     if _max > max_rob:
#         max_rob = _max
# print(house)