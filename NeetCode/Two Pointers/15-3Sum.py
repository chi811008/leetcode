class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            target = 0 - nums[i]
            # two sum
            head, tail = i + 1, len(nums)-1
            while head < tail:
                if nums[head] + nums[tail] == target:
                    res.append([nums[i], nums[head], nums[tail]])
                    print("got it")
                    print(head, tail)
                    head += 1
                    while (head < tail) and (nums[head] == nums[head - 1]):
                        head += 1
                elif nums[head] + nums[tail] > target:
                    tail -= 1
                elif nums[head] + nums[tail] < target:
                    head += 1
        return res

def runTest():
    solution = Solution()
    
    # Example 1
    nums = [-1,0,1,2,-1,-4]
    expected_output = [[-1,-1,2],[-1,0,1]]
    output = solution.threeSum(nums)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"
    
    # Example 2
    nums = [0, 1, 1]
    expected_output = []
    output = solution.threeSum(nums)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"
    
    # Example 3
    nums = [0, 0, 0]
    expected_output = [[0, 0, 0]]
    output = solution.threeSum(nums)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"
    
    print("All tests passed!")

if __name__ == "__main__":
    runTest()