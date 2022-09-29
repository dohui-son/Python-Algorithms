from collections import defaultdict,deque

star = ["  *  ", " * * ", "*****"]
n  = int(input().rstrip())
g = [[' ']*6500 for _ in range(3500)]

def rec(n, y, x):
    if n == 1:
        for i in range(3):
            for j in range(5): g[y+i][x+j] = star[i][j]
        return
    rec(n//2, y, x+3*n//2)
    rec(n//2, y+3*n//2,x)
    rec(n//2, y+3*n//2, x+3*n)

rec(n//3, 0, 0)
for i in range(n):
    for j in range(2*n-1) : print(*g[i][j],end="")
    print()