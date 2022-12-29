class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1 , rob2 = rob2, max(rob1 + n, rob2)
        return max(rob1, rob2)

nums = [1, 2, 3]
s = Solution().rob(nums)
print(s)