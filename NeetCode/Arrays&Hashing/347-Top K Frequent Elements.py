class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # bucket sort
        count = {}
        freq = [[] for _ in range(len(nums))]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for num, c in count.items():
            freq[c-1].append(num)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
def runTest():
    nums = [1]
    k = 1
    s = Solution()
    print(s.topKFrequent(nums, k))

if __name__ == "__main__":
    runTest()