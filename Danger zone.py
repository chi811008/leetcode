# 輸入包含 n+1 行，第一行爲數字 n，接下來 n 行為該國人民的活動範圍
n = int(input())
country = [[int(i) for i in input().split()] for j in range(n)]

# prefix
pre_left = float("-infinity")
pre_right = float("infinity")
res_left = [0] * n
res_right = [0] * n
for i in range(n):
    res_left[i] = pre_left
    res_right[i] = pre_right
    pre_left = max(pre_left, country[i][0])
    pre_right = min(pre_right, country[i][1])

# postfix
post_left = float("-infinity")
post_right = float("infinity")
max_interval = 0
for i in range(n - 1, -1, -1):
    # area = right - left
    max_interval = max(max_interval, min(post_right, res_right[i]) - max(post_left, res_left[i]))
    
    post_left = max(post_left, country[i][0])
    post_right = min(post_right, country[i][1])

print(max_interval)



with open("/Users/cuiyaqing/Desktop/problem_229_test_cases/6.in") as test:
    lines = test.read()
    lines = lines.split('\n')
    n = int(lines[0])
    country = [[int(j) for j in lines[i].split()] for i in range(1, len(lines) - 1)]
print(country)
print(len(country))