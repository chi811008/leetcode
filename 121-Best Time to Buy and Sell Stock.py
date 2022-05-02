prices = [1]
ans = 5
diff = list()
for i in range(1, len(prices)):
    diff.append(prices[i] - prices[i - 1])
print(diff)
# find the max subarray in diff
curr = max_profits = diff[0]
for i in range(1, len(diff)):
    curr += diff[i]
    if diff[i] > curr:
        curr = diff[i]
    if curr > max_profits:
        max_profits = curr
    
if max_profits < 0:
    max_profits = 0
print(max_profits)
    







# O(n2)
max_profits = 0
for i in range(len(prices)):
    for j in range(0, i):
        profits = prices[i] - prices[j]
        if profits > max_profits:
            max_profits = profits
print(max_profits)