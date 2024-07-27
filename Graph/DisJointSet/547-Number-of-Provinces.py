class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        
        cityRoot = [i for i in range(len(isConnected))]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                cityRoot[rootX] = rootY
        
        def find(x):
            if cityRoot[x] != x:
                cityRoot[x] = find(cityRoot[x])
            return cityRoot[x]
        
        for i in range(len(isConnected)-1):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)
                    
        province = set()
        for i in range(len(isConnected)):
            province.add(find(i)) 

        return len(province)

def runTests():
    test_cases = [
        ([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]], 8)
    ]
    for i, (isConnected, expected) in enumerate(test_cases):
        result = Solution().findCircleNum(isConnected)
        print(f"Test case {i+1}: {result == expected}")
if __name__ == "__main__":
	runTests()
 