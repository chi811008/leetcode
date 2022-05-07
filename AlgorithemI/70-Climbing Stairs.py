def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a = 1
    b = 2
    for i in range(1, n):
        a, b = b, a + b
    return a

ans = stairs(4)
print(ans)
