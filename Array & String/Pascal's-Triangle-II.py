class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        lastLayer = []
        for i in range(rowIndex+1):
            res = []
            if i == 0:
                res.extend([1])
            elif i == 1:
                res.extend([1, 1])
            else:
                for j in range(len(lastLayer)+1):
                    if j == 0:
                        res.append(lastLayer[j])
                    elif j == len(lastLayer):
                        res.append(lastLayer[len(lastLayer)-1])
                    else:
                        res.append(lastLayer[j]+lastLayer[j-1])
            lastLayer = res
        return res

def runTest():
    s = Solution()
    ans = s.getRow(4)
    print(ans)

if __name__ == '__main__':
    runTest()