class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        while nums[i] != 0:
            i += 1
        
        for j in range(i+1, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

def runTest():
	nums = [0,1,0,3,12]
	sol = Solution()
	sol.moveZeroes(nums)
	print(nums)
 
if __name__ == "__main__":
	runTest()
                