from collections import deque


class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        dic = {}
        q = deque(replacements)
        res = ""
        while q:
            key, val = q.popleft()
            if "%" in val:
                i = 0
                tmp = ""
                while i < len(val):
                    if val[i] == "%":
                        if val[i + 1] not in dic:
                            q.append([key, val])
                            break
                        tmp += dic[val[i + 1]]
                        i += 2
                    else:
                        tmp += val[i]
                    i += 1
                if i == len(val):
                    dic[key] = tmp
            else:
                dic[key] = val
        print(dic)
        i = 0
        while i < len(text):
            if text[i] == "%":
                res += dic[text[i + 1]]
                i += 2
            else:
                res += text[i]
            i += 1
        return res
