t = int(input())
for tt in range(t):
    n = int(input())
    coin = [*map(int, input().split())]
    money = int(input())
    dp = [0]*(money+1)
    dp[0] = 1
    for i in coin:
        for j in range(i, money+1):
            if j-i >= 0: dp[j] += dp[j-i] # 지금 코인이 i원짜리 일때, dp[j]번째에는 dp[j-i]에서 코인 i만 더해주면 j원이 된다
    print(dp[money])