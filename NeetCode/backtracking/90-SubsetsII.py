class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort()
        
        subset = []
        def dfs(i):
            if i > len(nums) - 1:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

def runTest():
    nums = [1,2,2]
    s = Solution()
    r = s.subsetsWithDup(nums)
    print(r)
    
if __name__ == '__main__':
    runTest()