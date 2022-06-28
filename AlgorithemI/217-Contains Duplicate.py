class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set()
        for num in nums:
            if num in unique_numbers:
                return True
            else:
                unique_numbers.add(num)
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = dict()
        for num in nums:
            if unique_numbers.get(num) == 1:
                return True
            else:
                unique_numbers[num] = 1
        return False

