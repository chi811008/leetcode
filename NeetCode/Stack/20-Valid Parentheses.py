class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(": ")", "[": "]", "{": "}"}
        container = list()
        for e in s:
            if e in parentheses:
                container.append(e)
            else:
                if container:
                    l = container.pop()
                    if e != parentheses[l]:
                        return False
                else:
                    return False

        if container:
            return False
        else:
            return True