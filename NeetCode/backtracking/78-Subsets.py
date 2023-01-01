# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         res = list()
#         subset = list()
#         def dfs(i):
#             if i > len(nums) - 1:
#                 res.append(subset.copy())
#                 return 
            
#             subset.append(nums[i])
#             dfs(i + 1)

#             subset.pop()
#             dfs(i + 1)
        
#         dfs(0)
#         return res
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = list()
        subset = list()
        def dfs(i):
            res.append(subset.copy())
            if i > len(nums) - 1:
                return

            for i in range(i, len(nums)):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        
        dfs(0)
        return res
nums = [1, 2, 3]
a = Solution().subsets(nums)
print(a)