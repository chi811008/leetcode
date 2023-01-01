class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = list()
        path = set()

        per = list()
        def dfs():
            if len(per) == len(nums):
                res.append(per.copy())
                return
                
            for i in range(len(nums)):
                if nums[i] not in path:
                    per.append(nums[i])
                    path.add(nums[i])
                    dfs()
                    path.remove(nums[i])
                    per.pop()
                
        dfs()
        return res

nums = [1, 2, 3]
s = Solution().permute(nums)
print(s)
