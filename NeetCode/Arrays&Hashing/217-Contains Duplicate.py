class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element = set()
        for ele in nums:
            if ele in element:
                return True 
            element.add(ele)
        return False