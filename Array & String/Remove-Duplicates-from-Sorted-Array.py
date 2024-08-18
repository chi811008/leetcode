class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                
        return i + 1

def runTest():
	nums = [0,0,1,1,2,2,3,3,4]
	sol = Solution()
	print(sol.removeDuplicates(nums))
	print(nums)

if __name__ == "__main__":
	runTest()