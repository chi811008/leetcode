n = 1
dp = [0] * (n + 1)

def st(n):
    dp[1] = 1
    if n == 1:
        return 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]
print(st(n))





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

ans = stairs(n)
print(ans)
