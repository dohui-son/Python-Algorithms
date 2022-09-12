from multiprocessing.connection import answer_challenge
import sys; sys.setrecursionlimit(7000); input = sys.stdin.readline
from collections import defaultdict,deque
global n,ans
ans = 0
tonum = defaultdict(int)

def bt(y, queens,left_x,left_y,right_x,right_y):
    global n,ans
    if y == n: ans += 1; return
    if y >n: return
    hoobo = ( (1<<n)-1 ) & ~queens
    while hoobo:
        nextt = hoobo & -hoobo
        hoobo &= ( hoobo-1 )
        x = tonum[nextt]
        ly,lx,ry,rx = 0, x-y,0,x+y
        nlx, nly, nrx, nry = 0,0,0,0
        if lx < 0: ly = -lx; lx = 0; nly = (1<<ly)
        else : nlx = (1<<lx)
        
        if rx >= n: ry = (rx+1-n); rx = n-1; nry = (1<<ry)
        else:  nrx = (1<<rx)

        if left_x & nlx or left_y & nly or right_x & nrx or right_y &nry : continue
        
        bt( y+1, queens|nextt, left_x | nlx, left_y | nly , right_x | nrx, right_y | nry )

n = int( input().rstrip() )
for i in range(n): tonum[ (1<<i) ] = i
bt(0,0,0,0,0,0)

print(ans)