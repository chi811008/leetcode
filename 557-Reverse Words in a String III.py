s = "Let's take LeetCode contest"
elements = [[c for c in e] for e in s.split()]
ans = list()
for e in elements:
    e.reverse()
    ans.append("".join(e))

print(" ".join(ans))

ans = []
for _ in s.split():
    tail = len(_) - 1
    _ans = ""
    while tail >= 0:
        _ans += _[tail]
        tail -= 1
    ans.append(_ans)
print(" ".join(ans))