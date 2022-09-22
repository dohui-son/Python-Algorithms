from collections import defaultdict, deque
global ans,g

n,m = map(int,input().split())
g = [input() for _ in range(n)]
INF = int(3e9)
ans = INF
def changeCol(col): return ('B' if col == 'W' else 'W')
def check(color,counterpart, y,x):
    global ans,g
    ret = 0
    for i in range(8):
        for j in range(8):
            if ret>ans: return
            if (i+j)%2 == 0: 
                if g[y+i][x+j] != color: ret+=1
            else: 
                if g[y+i][x+j] != counterpart: ret+=1
    ans = min(ans,ret)
    

for y in range(0,n-7):
    for x in range(0,m-7):
        check('B','W',y,x)
        check('W','B',y,x)
        if ans == 0: print(0);exit(0)
print(ans)