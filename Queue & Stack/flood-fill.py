class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows, colums = len(image), len(image[0])
        oriColor = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if (
                r < 0
                or r > rows - 1
                or c < 0
                or c > colums - 1
                or (r, c) in visited
                or image[r][c] != oriColor
            ):
                return

            visited.add((r, c))
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return

        dfs(sr, sc)
        return image


from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        oriColor = image[sr][sc]
        rows, cols = len(image), len(image[0])
        visited = set()
        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            nr, nc = q.popleft()

            for dr, dc in directions:
                r, c = nr + dr, nc + dc

                if (
                    r > rows - 1
                    or r < 0
                    or c > cols - 1
                    or c < 0
                    or image[r][c] != oriColor
                    or (r, c) in visited
                ):
                    continue

                visited.add((r, c))
                image[r][c] = color
                q.append((r, c))
        return image
