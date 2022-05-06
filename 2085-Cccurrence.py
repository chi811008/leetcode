s = "abcda"
t = "abcdea"
mapping = dict()
for c in s:
    mapping[c] = mapping.get(c, 0) + 1
for c in t:
    n = mapping.get(c, 0)   
    if n:
        mapping[c] -= 1
    else:
        print(c)