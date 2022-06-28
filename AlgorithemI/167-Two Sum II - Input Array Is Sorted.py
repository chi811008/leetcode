numbers = [2,7,11,15]
target = 9
mapping = dict()
for i in range(len(numbers)):
    c = mapping.get(numbers[i])
    if c:
        print([c, i + 1])
    else:
        mapping[target - numbers[i]] = i + 1

head = 0
tail = len(numbers) - 1
while head < tail:
    s = numbers[head] + numbers[tail]
    if s == target:
        print([head + 1, tail + 1])
    elif s > target:
        tail -=1
    elif s < target:
        head += 1
    
















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