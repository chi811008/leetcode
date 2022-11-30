from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = defaultdict(int)
        for index, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target-num], index]
            num_map[num] = index