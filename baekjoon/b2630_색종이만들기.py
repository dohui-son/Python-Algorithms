# 색종이 만들기
from collections import defaultdict,deque
from sys import setrecursionlimit, stdin; input = stdin.readline

setrecursionlimit(7000)

n = int(input().rstrip())
g = [[*map(int,input().split())] for _ in range(n)]

ans = [0,0]

def rec(y,x,siz):
    if siz == 1 or y+1==n or x+1==n : ans[ g[y][x] ] += 1
    else:
        pre = 0 if g[y][x] else 1
        flag = True
        for yy in range(y,y+siz): 
            if pre in g[yy][x:x+siz]: flag = False; break
        if flag : ans[g[y][x]] += 1
        else : 
            for yy in range(y,y+siz, siz//2):
                for xx in range(x,x+siz, siz//2): rec(yy,xx,siz//2)
    return

rec(0,0,n)
print(*ans, sep="\n")
