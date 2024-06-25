class Solution:
    def maxArea(self, height: list[int]) -> int:
        head, tail = 0, len(height) - 1
        maxRes = 0
        while head < tail:
            res = min(height[head], height[tail]) * (tail - head)
            maxRes = max(res, maxRes)
            if height[head] < height[tail]:
                head += 1
            elif height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
        return maxRes

def runTest():
    solution = Solution()
			
    # Example 1
    height1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    output1 = solution.maxArea(height1)
    assert output1 == expected1
    print(f"Example 1 - Input: {height1}, Output: {output1}, Expected: {expected1}")
			
    # Example 2
    height2 = [1,1]
    expected2 = 1
    output2 = solution.maxArea(height2)
    print(f"Example 2 - Input: {height2}, Output: {output2}, Expected: {expected2}")
			
if __name__ == "__main__":
	runTest()
       
       
