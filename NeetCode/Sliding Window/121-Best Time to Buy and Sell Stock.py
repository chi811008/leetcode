prices = [7,6,4,3,1]
l, r = 0, 0
max_profits = 0
while r < len(prices) - 1:
    r += 1
    profits = prices[r] - prices[l]
    if profits > max_profits:
        max_profits = profits
    if prices[r] < prices[l]:
        l = r

print(max_profits)










# if len(prices) == 1:
#     print(0)
# else:
#     prediff = prices[-1] - prices[-2]
#     ans = prediff if prediff > 0 else 0
#     for i in range(len(prices) - 2, 0, -1):
#         diff = prices[i] - prices[i - 1]
#         prediff = max(prediff + diff, diff)
#         if prediff > ans:
#             ans = prediff
#     print(ans)
