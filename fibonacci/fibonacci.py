def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return f(n - 1) + f(n - 2)
def f_func(n):
    dp = [0, 1]
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    for i in range(2, n):
        dp.append(dp[i - 2] + dp[i - 1])
    return dp[-1]
print(f_func(10))