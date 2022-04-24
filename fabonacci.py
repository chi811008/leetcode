def fabonacci(n):
    a = 1
    b = 1
    for i in range(1, n + 1):
        yield a
        a, b = b, a + b

for num in fabonacci(10):
    print(num)