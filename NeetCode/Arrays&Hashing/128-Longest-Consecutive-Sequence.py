class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        # visited = set()
        maxLength = 0
        # for n in nums:
        #     if n not in visited:
        #         count = 1
        #         visited.add(n)
        #         while n + 1 in nums:
        #             count += 1
        #             n += 1
        #             visited.add(n)
        #         maxCount = max(count, maxCount)
        # return maxCount
        for n in nums:
            if n - 1 not in nums: # a start sequence
                length = 0
                while n + length in nums:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength

                

def runTest():
    nums = [100,4,200,1,3,2]
    s = Solution()
    print(s.longestConsecutive(nums))

if __name__ == "__main__":
    runTest()
                
