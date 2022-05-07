n = "00000000000000000000000000001011"
ans = 0
for c in str(n):
    print(c)
    if c == "1":
        ans += 1
print(ans)