#경사로
from collections import deque, defaultdict
global n,L, ans
ans = 0
n,L = map(int, input().split())
g = [ [*map(int,input().split())] for _ in range(n)]
gg = [ [0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        gg[i][j] = g[j][i]

def BF(arr):
    global n, L, ans
    for i in range(n):
        cnt = 1
        j = 0
        for jj in range(n):
            j = jj
            if j == n-1: break
            if arr[i][j] == arr[i][j+1] : cnt +=1
            elif arr[i][j] + 1 == arr[i][j+1] and cnt>=L : cnt = 1
            elif arr[i][j] -1 == arr[i][j+1] and cnt >= 0 : cnt = 1-L
            else : break
        if j == n-1 and cnt>=0 : ans += 1
    return

BF(g)
BF(gg)

print(ans)