class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        res = []
        
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                tmp = [1]
                for j in range(1, len(res[-1])):
                    tmp.append(res[-1][j-1] + res[-1][j])
                tmp.append(1)
                res.append(tmp)
        return res


def runTest():
    numRows = 5
    obj = Solution()
    result = obj.generate(numRows)
    print(result)
    assert result == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

if __name__ == '__main__':
	runTest()