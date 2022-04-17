nums = [3,1,2,2,2,1,3]
k = 2
ans = 4

ans = 0
imap = dict()
for i, value in enumerate(nums):
    if value in imap:
        for ind in imap[value]:
            print(ind, i)
            if (i * ind % k) == 0:
                ans += 1
    indices = imap.get(value, [])
    indices.append(i)
    imap[value] = indices

print(ans)
