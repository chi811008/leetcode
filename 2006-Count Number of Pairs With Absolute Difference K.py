nums = [1,2,2,1]
k = 1


dif = dict()
ans = 0
for num in nums:
    if num in dif:
        ans += dif[num]
    dif[num + k] = dif.get(num + k, 0) + 1
    dif[num - k] = dif.get(num - k, 0) + 1
print(ans)
# {1:2, 5:2, 0:1, 4:1, -1:1, 3:2, 7:1, 2:1, 6:1}

# 5! +1
# 4! +1
# 3! +2
# 3 2 1  5 4 3 1

# 1 0 -1 3 2 1
# 5 4 3  7 6 5