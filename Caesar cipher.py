s = "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwV ALD"
secret = "Vjh cqn Oxaln kn frcq hxd!"
upper_hash = {i:chr(ord("A") + i) for i in range(26)}
lower_hash = {i:chr(ord("a") + i) for i in range(26)}
for i in range(1, 26):
    ans = ""
    for c in secret:
        if c.islower():
            ans += lower_hash[(ord(c) - ord("a") + i) % 26]
        elif c.isupper():
            ans += upper_hash[(ord(c) - ord("A") + i) % 26]
        else:
            ans += c
    print(i, ans)
