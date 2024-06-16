class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        elements = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in elements.keys():
                return [i, elements[res]]
            elements[nums[i]] = i


def runTest():
    s = Solution()
    nums = [3,2,3]
    target = 6
    print(s.twoSum(nums, target))

if __name__ == "__main__":
    runTest()
            
            