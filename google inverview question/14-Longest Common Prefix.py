class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        prefix = ""

        for i in range(1, len(strs)):
            if len(pre) < len(strs[i]):
                pre, strs[i] =  strs[i], pre
            for j in range(len(strs[i])):
                if pre[j] == strs[i][j]:
                    prefix += pre[j]
                else:
                    break
            pre = prefix
            prefix = ""
        return pre
                