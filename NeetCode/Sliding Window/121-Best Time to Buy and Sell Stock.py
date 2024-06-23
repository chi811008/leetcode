class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        smallIdx, maxPro = 0, 0
        for i in range(1, len(prices)):
            maxPro = max(prices[i]-prices[smallIdx], maxPro)
            if prices[i] < prices[smallIdx]:
                smallIdx = i
        return maxPro

def runTest():
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
    tests = (
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1, 1, 1, 1], 0)
    )
    s = Solution()
    for t, output in tests:
        val = s.maxProfit(t)
        assert val == output

if __name__ == "__main__":
    runTest()