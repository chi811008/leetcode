class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre, post, res = 1, 1, []
        for i in range(len(nums)):
            res.append(pre)
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
            
def runTest():
    l = [1, 2, 3, 4]
    s = Solution()
    print(s.productExceptSelf(l))
    
if __name__ == "__main__":
    runTest()
    