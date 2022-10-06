from collections import defaultdict, deque
import sys; sys.setrecursionlimit(10000)
n = int(input().rstrip())
c = 5*(n//3) + (n//3-1)

g = [[' ']*c for _ in range(n)]
sy, sx = 0, c//2
print(n,c)
def printstar(cnt,y,x, isLeft, haveChild):
    g[y][x] = '*'
    g[y+1][x-1] = '*'
    g[y+1][x+1] = '*'
    g[y+2][x] = '*'
    g[y+2][x-1] = '*'
    g[y+2][x-2] = '*'
    g[y+2][x+1] = '*'
    g[y+2][x+2] = '*'
    
    if haveChild and cnt<n//3:
        
        if cnt%2==1 and cnt%4 == 3:
            if isLeft:
                printstar(cnt+1, y+3, x-3, True, True)
                printstar(cnt+1, y+3, x+3, False, False)
            else:
                printstar(cnt+1, y+3, x-3, True, False)
                printstar(cnt+1, y+3, x+3, False, True)
        elif cnt%2==1:
            printstar(cnt+1, y+3, x-3, True, True)
            printstar(cnt+1, y+3, x+3, False, True)
        else:
            if isLeft : printstar(cnt+1, y+3, x-3, True, True)
            else:printstar(cnt+1, y+3, x+3, False, True)


printstar(1, sy, sx, False, True)
for i in g: print(*i, sep="")
