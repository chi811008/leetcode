class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        layer = 0
        
        rows, cols = len(matrix), len(matrix[0])
        res = []
        
        while len(res) < rows * cols:
            for c in range(layer, cols-layer):
                res.append(matrix[layer][c])
            if len(res) == rows * cols:
                break
            
            for r in range(layer+1, rows-layer):
                res.append(matrix[r][cols-1-layer])
            if len(res) == rows * cols:
                break
            
            for c in range(cols-1-layer-1, layer-1, -1):
                res.append(matrix[rows-1-layer][c])
            if len(res) == rows * cols:
                break
            
            for r in range(rows-1-layer-1, layer, -1):
                res.append(matrix[r][layer])
            if len(res) == rows * cols:
                break
            
            layer += 1
        return res
            
def runTest():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    obj = Solution()
    result = obj.spiralOrder(matrix)
    print(result)
    assert result == [1,2,3,4,8,12,11,10,9,5,6,7]
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    result = obj.spiralOrder(matrix)
    print(result)
    assert result == [1,2,3,6,9,8,7,4,5]
 
if __name__ == '__main__':
	runTest()
