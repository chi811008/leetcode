# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_map = dict()
#         for i in range(len(nums)):
#             num_map.update({nums[i]: i})
#             if (target - nums[i]) in num_map:
#                 return [num_map.get(target - nums[i]), i]
nums = [3,2,4]
target = 6
num_map = dict()
for i in range(len(nums)):
    if (target - nums[i]) in num_map:
        print([num_map.get(target - nums[i]), i])
    num_map.pdate({nums[i]: i})