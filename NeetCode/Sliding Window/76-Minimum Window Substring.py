from collections import defaultdict
s = "a"
t = "aa"
mapt = defaultdict(int)
maps = defaultdict(int)
for c in t:
    mapt[c] += 1
need = len(mapt)
min_length = len(s)
min_string = ""
l, have = 0, 0

for r in range(len(s)):
    print(s[r])
    if s[r] in mapt:
        maps[s[r]] += 1
        print(maps)
        if maps.get(s[r]) == mapt[s[r]]:
            have += 1
        print(f"have: {have}")
        while have == need:
            while s[l] not in mapt:
                l += 1
            print(s[l])
            maps[s[l]] -= 1
            print(maps)
            if maps.get(s[l]) < mapt.get(s[l]):
                have -= 1
                print(f"have: {have}")
            if (r - l + 1) <= min_length:
                min_length = r - l + 1
                min_string = s[l:r + 1]
            print(f"min_length: {min_length}")
            l += 1
print(min_length)
print(min_string)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapt = defaultdict(int)
        maps = defaultdict(int)
        for c in t:
            mapt[c] += 1
        need = len(mapt)
        min_length = len(s)
        min_string = ""
        l, have = 0, 0

        for r in range(len(s)):
            if s[r] in mapt:
                maps[s[r]] += 1
                if maps.get(s[r]) == mapt[s[r]]:
                    have += 1
                while have == need:
                    while s[l] not in mapt:
                        l += 1
                    maps[s[l]] -= 1
                    if maps.get(s[l]) < mapt.get(s[l]):
                        have -= 1
                    if (r - l + 1) <= min_length:
                        min_length = r - l + 1
                        min_string = s[l:r + 1]
                    l += 1
        return min_string