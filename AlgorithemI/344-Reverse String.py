s = ["h","e","l","l","o"]
head, tail = 0, len(s) - 1
while head <= tail:
    s[head], s[tail] = s[tail], s[head]
    head += 1
    tail -= 1
print(s)