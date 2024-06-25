class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        head, tail = 0, len(numbers) - 1
        while head < tail:
            if (numbers[head] + numbers[tail]) == target:
                return [head + 1, tail + 1]
            elif ((numbers[head] + numbers[tail]) < target) and (head < tail):
                head += 1
            elif ((numbers[head] + numbers[tail]) > target) and (head < tail):
                tail -= 1
	
def runTest():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    result = s.twoSum(nums, target)
    assert result == [1, 2], f"Expected [1, 2], but got {result}"

    nums = [2, 3, 4]
    target = 6
    result = s.twoSum(nums, target)
    assert result == [1, 3], f"Expected [1, 3], but got {result}"

    nums = [-1, 0]
    target = -1
    result = s.twoSum(nums, target)
    assert result == [1, 2], f"Expected [1, 2], but got {result}"
    
    nums = [3,24,50,79,88,150,345]
    target = 200
    result = s.twoSum(nums, target)
    assert result == [3,6], f"Expected [3,6], but got {result}"
    

if __name__ == "__main__":
    runTest()