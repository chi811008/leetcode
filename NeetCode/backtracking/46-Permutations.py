class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

class Solution2:
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