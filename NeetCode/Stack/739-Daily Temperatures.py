temperatures = [89,62,70,58,47,47,46,76,100,70]
# ans = [8,1,5,4,3,2,1,1,0,0]
res = [0] * len(temperatures)
index_temperature = list()

for index, temperature in enumerate(temperatures):
    while index_temperature and temperature > index_temperature[-1][1]:
        pre_index, pre_temperature = index_temperature.pop()
        res[pre_index] = index - pre_index
    index_temperature.append((index, temperature))
print(res)
