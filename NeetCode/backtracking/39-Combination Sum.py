class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = list()

        combination = list()
        def dfs(i, residule):
            if residule == 0:
                res.append(combination.copy())
                return
            elif residule < 0 or i > len(candidates) - 1:
                return
            else:

                combination.append(candidates[i])
                dfs(i, residule - candidates[i])

                combination.pop()
                dfs(i + 1, residule)

        dfs(0, target)
        return res

candidates = [2,3,6,7]
target = 7
r = Solution().combinationSum(candidates, target)
print(r)