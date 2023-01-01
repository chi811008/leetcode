class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = list()
        nums.sort()

        subset = list()
        def dfs(i):
            print(i)
            if i > len(nums) - 1:
                res.append((subset.copy()))
                return
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            
            # All subsets that exclude nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            dfs(i + 1)
    
        dfs(0)
        return res

            

nums = [1, 2, 2]
a = Solution().subsetsWithDup(nums)
print(a)
