class Solution(object):
    def trap(self, height):
        print(f'height: {height}')
        maxLeft, maxRight = 0, 0
        res = 0
        head, tail = 0, len(height) - 1
        while head <= tail:
            print(f'head: {head}, tail: {tail}')
            print(f'maxLeft: {maxLeft}, maxRight: {maxRight}')
            print(f'height[head]: {height[head]}, height[tail]: {height[tail]}')
            if maxLeft <= maxRight:
                area = maxLeft - height[head]
                maxLeft = max(maxLeft, height[head])
                head += 1
            else:
                area = maxRight - height[tail]
                maxRight = max(maxRight, height[tail])
                tail -= 1
            if area > 0:
                res += area
            print(f'area: {area}', f'res: {res}')
   
        return res

def test_trap():
	s = Solution()
	testCases = [
		([0,1,0,2,1,0,1,3,2,1,2,1], 6),
		([4,2,0,3,2,5], 9),
		([4,2,3], 1)
	]	
	for height, solution in testCases:
		print(height, solution)
		res = s.trap(height)
		assert res == solution
  
if __name__ == '__main__':
	test_trap()
            
            
            
     
        
        
