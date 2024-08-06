class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(l, head, tail):
            while head < tail:
                l[head], l[tail] = l[tail], l[head]

                head += 1
                tail -= 1
        
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)