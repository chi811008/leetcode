class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = list()
        candidates.sort()
        print(candidates)

        subset = list()
        def dfs(i, residule):
            if residule == 0:
                res.append(subset.copy())
                return
            elif residule < 0 or i > len(candidates) - 1:
                return
            else:
            
                subset.append(candidates[i])
                dfs(i + 1, residule - candidates[i])
                subset.pop()

                while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                    i += 1
                dfs(i + 1, residule)

        dfs(0, target)
        return res
candidates = [10,1,2,7,6,1,5]
target = 8
a = Solution().combinationSum2(candidates, target)
print(a)
