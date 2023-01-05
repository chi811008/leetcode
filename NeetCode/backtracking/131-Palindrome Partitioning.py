class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = list()

        subs = list()
        def dfs(j):
            if j == len(s):
                res.append(subs.copy())
                return
        
            for i in range(j, len(s)):
                if self.is_palindrome(s[j:i + 1]):
                    subs.append(s[j:i + 1])
                    dfs(i + 1)
                    subs.pop()
        dfs(0)
        return res

    def is_palindrome(self, substring):
        head, tail = 0, len(substring) - 1

        while head < tail:
            if substring[head] != substring[tail]:
                return False
            head += 1
            tail -= 1
        return True
a = Solution().partition("aab")
print(a)

def is_palindrome(substring):
    head, tail = 0, len(substring) - 1

    while head < tail:
        if substring[head] != substring[tail]:
            return False
        head += 1
        tail -= 1
    return True
s = "aab"
res = list()
subs = list()
def find_substring(j):
    if j == len(s):
        res.append(subs.copy())
        return
    for i in range(j, len(s)):
        print(s[j :i + 1], s[i + 1:])
        if is_palindrome(s[j :i + 1]):
            subs.append(s[j :i + 1])
            find_substring(i + 1)
            subs.pop()
    return res
a = find_substring(0)
print(a)