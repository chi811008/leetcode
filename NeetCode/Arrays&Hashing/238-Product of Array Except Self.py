class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre, post = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
