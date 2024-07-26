class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        rows = len(mat)
        columns = len(mat[0])
        res = []
        reverse = False
        for r in range(rows):
            c = 0
            tmp = []
            while r >= 0 and (c <= columns - 1):
                tmp.append(mat[r][c])
                r -= 1
                c += 1
            if reverse:
                res.extend(tmp[::-1])
                reverse = False
            else:
                res.extend(tmp)
                reverse = True

        for c in range(1, columns):
            r = rows - 1
            tmp = []
            while r >= 0 and (c <= columns - 1):
                tmp.append(mat[r][c])
                r -= 1
                c += 1
            if reverse:
                res.extend(tmp[::-1])
                reverse = False
            else:
                res.extend(tmp)
                reverse = True
        return res
    
class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        r, c = 0, 0       
        up = True
        res = []
        
        while len(res) < rows * cols:
        
            if up:
                # up
                while r >= 0 and c < cols:
                    res.append(mat[r][c])

                    r -= 1
                    c += 1

                if c == cols:
                    r += 2
                    c -= 1
                else:
                    r += 1
                
                up = False

            else:
                # down
                while r < rows and c >= 0:
                    res.append(mat[r][c])

                    r += 1
                    c -= 1

                if r == rows:
                    r -= 1
                    c += 2
                else:
                    c += 1
                
                up = True
        return res

if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    print(obj.findDiagonalOrder(mat))
    mat = [[2,5,8],[4,0,-1]]
    obj = Solution()
    print(obj.findDiagonalOrder(mat))
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    obj = Solution()
    print(obj.findDiagonalOrder(mat))
