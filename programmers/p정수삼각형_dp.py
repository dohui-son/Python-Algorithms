def solution(triangle):
    ans = 0
    dp = [[0 for i in t] for t in triangle]
    for y, row in enumerate(triangle):
        if y == 0: dp[0][0] = triangle[0][0]; continue
        for x, val in enumerate(row):
            if x == 0 : dp[y][x] =  triangle[y][x] + dp[y-1][x]
            elif x == len(row)-1: dp[y][x] =  triangle[y][x] + dp[y-1][x-1]
            else :dp[y][x] = max(triangle[y][x] + dp[y-1][x-1], triangle[y][x] + dp[y-1][x])
    return max(dp[-1])