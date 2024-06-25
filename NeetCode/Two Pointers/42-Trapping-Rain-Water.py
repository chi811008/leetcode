class Solution:
    def trap(self, height: list[int]) -> int:
        head, tail = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        maxRes = 0
        while head < tail:
            res = min(maxLeft, maxRight) - height[head]
            print(f"height[head]: {height[head]},height[tail]:{height[tail]}, maxLeft: {maxLeft}, maxRight: {maxRight} res: {res}")
            if res > 0:
                maxRes += res
            maxLeft = max(maxLeft, height[head])
            if maxLeft <= maxRight:
                print(f"maxLeft: {maxLeft}, maxRight: {maxRight}, maxRes: {maxRes}")	
                head += 1
            else:
                tail -= 1
            while (maxRight < maxLeft) & (head < tail):
                res = min(maxLeft, maxRight) - height[tail]
                if res > 0:
                    maxRes += res
                maxRight = max(maxRight, height[tail])
                print(f"height[head]: {height[head]},height[tail]:{height[tail]}, maxLeft: {maxLeft}, maxRight: {maxRight} res: {res}")
                if maxLeft <= maxRight:
                    print(f"maxLeft: {maxLeft}, maxRight: {maxRight}, maxRes: {maxRes}")
                    head += 1
                else:
                    tail -= 1
            # compare maxLeft & maxRight, pick min to go head
        return maxRes

def runTest():
    #input [4,2,0,3,2,5] expected = 9
    solution = Solution()
    height = [4,2,0,3,2,5]
    expected = 9
    output = solution.trap(height)
    print(f"Input: {height}, Output: {output}, Expected: {expected}")
    assert output == expected
 
if __name__ == "__main__":
	runTest()