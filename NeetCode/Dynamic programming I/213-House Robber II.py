class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(ls):
            pre, post = 0, 0

            for n in ls:
                pre, post = post, max(pre + n, post)
            return max(pre, post)

        return max(nums[0], helper(nums[1:]), helper(nums[: len(nums) - 1]))
