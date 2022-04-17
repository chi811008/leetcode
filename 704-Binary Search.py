nums = [-1,0,3,5,9,12]
target = 9

class Solution:
    def search(self, nums, target) -> int:
        head, tail = 0, len(nums) - 1
        def bs(head, tail, target, nums):
            if head > tail:
                return -1

            if nums[head] == target:
                return head
            elif nums[tail] == target:
                return tail
            else:
                mid = (head + tail) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return bs(mid + 1, tail - 1, target, nums)
                else:
                    return bs(head + 1, mid - 1, target, nums)
        return bs(head, tail, target, nums)


class Solution:
    def search(self, nums,  target: int) -> int:
        head, tail = 0, len(nums) - 1
        while head <= tail:
            if nums[head] == target:
                return head
            elif nums[tail] == target:
                return tail
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid
                head += 1
            else:
                head = mid
                tail -= 1
        return -1