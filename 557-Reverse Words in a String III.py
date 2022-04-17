s = "Let's take LeetCode contest"
a = "s'teL ekat edoCteeL tsetnoc"
ans = []
for _ in s.split():
    tail = len(_) - 1
    _ans = ""
    while tail >= 0:
        _ans += _[tail]
        tail -= 1
    ans.append(_ans)
print(" ".join(ans))