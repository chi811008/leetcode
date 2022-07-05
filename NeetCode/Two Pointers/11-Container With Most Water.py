height = [1,8,6,2,5,4,8,3,7]
head, tail = 0, len(height) - 1

ans = 0
while head < tail:
    area = min(height[head], height[tail]) * (tail - head)
    ans = max(area, ans)
    if height[head] > height[tail]:
        tail -= 1
    elif height[head] < height[tail]:
        head += 1
    else:
        if height[head + 1] > height[tail - 1]:
            head += 1
        elif height[head + 1] < height[tail - 1]:
            tail -= 1
        else:
            head += 1
print(ans)