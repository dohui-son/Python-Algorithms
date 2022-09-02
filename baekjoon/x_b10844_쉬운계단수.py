n = int(input().rstrip())
ans, mult = 0, 1000000000
memo = [[0]*10 for _ in range(100)]

for i in range(1,10): memo[0][i] = 1
for i in range(1,n):
    for j in range(0,10):
        if j == 0 : memo[i][j] = memo[i-1][j+1] % mult
        elif j == 9 : memo[i][j] = memo[i-1][j-1] % mult
        else : memo[i][j] = (memo[i-1][j-1] % mult + memo[i-1][j+1] % mult ) % mult

for i in range(10) : 
    ans += memo[n-1][i]
    ans %= mult
print(ans)