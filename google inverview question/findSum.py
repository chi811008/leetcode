# https://www.youtube.com/watch?v=XKu_SEDAykw
class Solution:
    def findSum(self, numbers: List, target: int) -> bool:
        head, tail = 0, len(numbers) -1

        while head < tail:
                if numbers[head] + numbers[tail] == target: return True

                if numbers[head] + numbers[tail] > target:
                   tail -= 1
                else:
                   head += 1
         
        return False


class Solution2:
    def findSum(self, numbers: list, target: int) -> bool:
        pairSet = set()
        
        for i in range(len(numbers)):
            pair = target - numbers[i]
            if pair in pairSet:
                return True
            pairSet.add(pair)

        return False

