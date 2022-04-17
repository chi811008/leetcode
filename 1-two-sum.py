nums = [2,7,11,15]
target = 9
imap = dict()
for i, value in enumerate():
    if value in imap:
        print(imap[value], i)
    imap[target - value] = i