class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = dict()
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        # bucket sort
        bucket = [[] for i in range(len(nums))]
        for key, value in num_map.items():
            bucket[value - 1].append(key)
        ans = list()
        for i in range(len(nums) - 1, -1, -1):
            if bucket[i]:
                ans.extend(bucket[i])
                if len(ans) == k:
                    return ans
nums = [1,1,1,2,2,3,100]
k = 2
num_map = dict()
for num in nums:
    num_map[num] = num_map.get(num, 0) + 1
# bucket sort
bucket = [[] for i in range(len(nums))]
for key, value in num_map.items():
    bucket[value - 1].append(key)
ans = list()
for i in range(len(nums) - 1, -1, -1):
    if bucket[i]:
        if len(ans) < k:
            ans.extend(bucket[i])
return ans
