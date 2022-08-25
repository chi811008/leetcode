import math
piles = [1,1,1,999999999]
h = 10
max_num = max(piles)
min_speed = max_num
def bs(head, tail, min_speed):
    mid = (head + tail) // 2
    if head > tail:
        return mid + 1
    count = 0
    for banana in piles:
        count += math.ceil(banana / mid)
    if count == h:
        min_speed = min(min_speed, mid)
        return bs(head, mid - 1, min_speed)
    elif count > h:
        return bs(mid + 1, tail, min_speed)
    elif count < h:
        return bs(head, mid - 1, min_speed)
ans = bs(1, max_num, min_speed)
print(ans)