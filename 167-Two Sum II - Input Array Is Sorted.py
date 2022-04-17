numbers = [-1,0]
ans     = [9,7,2,-2,-4]
target = -1
head = 0
tail = len(numbers) - 1
while head <= tail: 
    diff = target - numbers[head]
    if diff == numbers[tail]:
        print(head + 1, tail + 1)
        break
    elif diff > numbers[tail]:
        head += 1
    else:
        tail -= 1