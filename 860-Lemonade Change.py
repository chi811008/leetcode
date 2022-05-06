bills = [5,5,10,10,20]
ans = True
c = 5
mapping = dict()

for m in bills:
    mapping[m] = mapping.get(m, 0) + 1
    r = m - c
    if r == 0:
        continue
    if r == 5:
        if mapping.get(5, 0):
            mapping[5] -= 1
        else:
            return False
    elif r == 15:
        if (mapping.get(10, 0) >= 1) and (mapping.get(5, 0) >= 1):
            mapping[10] -= 1
            mapping[5] -= 1
        elif mapping.get(5, 0) >= 3:
            mapping[5] -= 3
        else:
            return False
return True