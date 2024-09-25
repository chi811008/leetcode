class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s

                residual = target - square
                if residual < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]


class SolutionDFS:
    def numSquares(self, n: int) -> int:
        res = n

        def dfs(i, squares, total):
            nonlocal res
            if total == 0:
                res = min(res, len(squares))
                print(squares)
                return
            elif total < 0 or i * i > total:
                return

            square = i * i
            squares.append(square)
            dfs(i, squares, total - square)
            squares.pop()

            dfs(i + 1, squares, total)

        dfs(1, [], n)
        return res


def runTest():
    n = 214
    s = SolutionDFS()
    r = s.numSquares(n)
    print(r)


if __name__ == "__main__":
    runTest()
