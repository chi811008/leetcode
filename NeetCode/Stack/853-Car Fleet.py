target = 100
position = [0,2,4]
speed = [4,2,1]

position_time = [(p, (target - p)/t ) for p , t in zip(position, speed)]
position_time.sort(key=lambda x: x[0], reverse=True)
fleet = list()
for p, t in position_time:
    if fleet:
        pre_p, pre_t = fleet[-1]
        if t > pre_t:
            fleet.append((p, t))
    else:
        fleet.append((p, t))
ans = len(fleet)
print(ans)