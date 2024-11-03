class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(total, i):
            if i == len(nums):
                return 1 if total == target else 0

            if (total, i) in dp:
                return dp[(total, i)]

            dp[(total, i)] = dfs(total + nums[i], i + 1) + dfs(total - nums[i], i + 1)

            return dp[(total, i)]

        return dfs(0, 0)
