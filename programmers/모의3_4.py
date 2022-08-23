from collections import defaultdict, deque
from sys import setrecursionlimit
setrecursionlimit(10000)
global g,dic,ans,n
INF = int(2e9)
ans = 0
g = []
se = set()


def BT(cur, bright, cnt,dic):
    global g,ans,se
    flag = True
    for i,val in enumerate(dic):
        if (1<<i)&bright == 0 and val&bright == 0: flag=False;break
    if flag:
        ans = min(ans, bin(bright).count('1'))
        return ans
    else:return -1
    # BT(cur+1, bright, cnt, dic)
    # BT(cur+1, bright|(1<<cur), cnt+1, dic)
    

def solution(N, light):
    global g,dic,ans,n
    ans = N
    n = N
    dic = [0]*n
    for l in light:
        a,b = l; a,b = a-1,b-1#; g[a].append(b); g[b].append(a)
        dic[a] |= (1<<b); dic[b] |= (1<<a) 
    for i in range( (1<<n)-1 ):
        
        res =  BT(0, i, 0,dic)
        if res>-1:break
    
    return ans