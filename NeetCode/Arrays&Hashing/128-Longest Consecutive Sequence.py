nums = [0,3,7,2,5,8,4,6,0,1]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in hash_nums: # num is start number
                length = 0
                while num + length in hash_nums:
                    length += 1
                longest = max(length, longest)
        return longest