class Solution:
    def isValid(self, s: str) -> bool:
        container = list()
        for e in s:
            if e in ["(", "[", "{"]:
                container.append(e)
            else:
                if container:
                    l = container.pop()
                    if (e == ")" and l != "(") or (e == "]" and l != "[") or (e == "}" and l != "{"):
                        return False
                else:
                    return False

        if container:
            return False
        else:
            return True