def solution(m, n, puddles):
    memo = [[0] * m for _ in range(n)]
    memo[0][0] = 1
    for y in range(n):
        for x in range(m):
            if [x + 1, y + 1] in puddles: continue
            if y > 0: memo[y][x] += memo[y - 1][x]%1000000007
            if x > 0: memo[y][x] += memo[y][x - 1]%1000000007
    return memo[n - 1][m - 1]%1000000007