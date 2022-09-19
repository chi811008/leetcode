nums = [1,3,4,2,2]
numbers = set()
for num in nums:
    if num in numbers:
        print(num)
    else:
        numbers.add(num)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if nums[fast] == nums[slow]:
                break
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow = nums[slow]
            slow2 = nums[slow2]
        return nums[slow2]