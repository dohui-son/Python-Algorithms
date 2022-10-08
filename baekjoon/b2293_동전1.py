from collections import defaultdict, deque
n, k = map(int,input().split())
coins = [0]*n
for nn in range(n): coins[nn] = int(input())
coins.sort()
dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for total in range(coin, k+1): dp[total] += dp[total-coin]
print(dp[k])