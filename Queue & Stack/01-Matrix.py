from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            nr, nc = q.popleft()
            for dr, dc in direction:
                r, c = nr + dr, nc + dc
                if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or (r, c) in visited:
                    continue

                mat[r][c] = mat[nr][nc] + 1
                q.append((r, c))
                visited.add((r, c))
        return mat


def runTests():
    s = Solution()
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
    ]
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
        [2, 3, 2],
    ]
    assert s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
        [2, 3, 2],
        [3, 4, 3],
    ]
    assert s.updateMatrix(
        [[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    ) == [[0, 0, 0], [0, 1, 0], [1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4]]
    assert s.updateMatrix(
        [[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    ) == [[0, 0, 0], [0, 1, 0], [1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5]]


if __name__ == "__main__":
    runTests()
