def fabonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


f_map = {1:1, 2:1}
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    if f_map.get(n):
        number = f_map.get(n)
    else:
        number = f(n - 1) + f(n - 2)
    f_map[n] = number
    print(n, number)
    return number
n = 20
a = f(n)
print(a)
for num in fabonacci(n):
    print(num)