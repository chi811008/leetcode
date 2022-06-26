coins = [2,5,10,1]
amount = 27
min_coin = amount + 1
coin_nums = [min_coin] * (amount + 1)
coin_nums[0] = 0

for a in range(1, amount + 1):
    for c in coins:
        result = a - c
        if result >= 0:
            method = 1 + coin_nums[result]
            if method < coin_nums[a]:
                coin_nums[a] = method
print(coin_nums[amount] if (coin_nums[amount] < (amount + 1)) else -1)