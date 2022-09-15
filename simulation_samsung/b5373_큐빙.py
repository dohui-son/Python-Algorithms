#큐빙- 2시간 6분

# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색

from collections import defaultdict, deque
from copy import deepcopy
#        0   1    2   3   4  5
color = ['w','y','r','o','g','b']
who = defaultdict(list)
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
# 윗 면은 흰색 0, 아랫 면은 노란색 1, 앞 면은 빨간색 2, 뒷 면은 오렌지색 3,
# 왼쪽 면은 초록색 4, 오른쪽 면은 파란색 5

# col, idx, isGaro, rev):
# 색상 몇번째줄? 가로인가 거꾸로
ga,se = True, False
rev, cor = True,False
# 위
who['U'] = [(3,0,ga,rev),(5,0,ga, rev),(2,0, ga,rev),(4,0,ga,rev)]
# 아래
who['D'] = [(3,2,ga,cor),(4,2,ga,cor),(2,2,ga,cor),(5,2,ga,cor)]
# 앞
who['F'] = [(0,2,ga,cor),(5,0,se,cor),(1,2,ga,cor),(4,2,se,rev)]
# 뒤
who['B'] = [(0,0,ga,rev),(4,0,se,cor),(1,0,ga,rev),(5,2,se,rev)]
# 왼
who['L'] = [(0,0,se,cor),(2,0,se,cor),(1,2,se,rev),(3,2,se,rev)]
# 오
who['R'] = [(0,2,se,rev),(3,0,se,cor),(1,0,se,cor),(2,2,se,rev)]


tonum = defaultdict(int)
tonum['U'] = 0
tonum['D'] = 1
tonum['F'] = 2
tonum['B'] = 3
tonum['L'] = 4
tonum['R'] = 5
t = int(input().rstrip())

def reading(col, idx, isGaro, rev):
    ret = deque()
    if not isGaro: #세로
        if rev: #거꾸로
            for i in range(2,-1,-1): ret.append(cube[col][i][idx])
        else:
            for i in range(3): ret.append(cube[col][i][idx])

    else: #가로
        if rev:ret.extend(cube[col][idx][::-1])
        else:ret.extend(cube[col][idx])
    return ret

def reading(col, idx, isGaro, rev):
    ret = deque()
    if not isGaro: #세로
        if rev: #거꾸로
            for i in range(2,-1,-1): ret.append(cube[col][i][idx])
        else:
            for i in range(3): ret.append(cube[col][i][idx])
    else: #가로
        if rev:ret.extend(cube[col][idx][::-1])
        else:ret.extend(cube[col][idx])
    return ret

def reader(ch):
    l = who[ch]
    ret = deque()
    for ll in l:
        q = reading(ll[0], ll[1], ll[2], ll[3])
        ret.extend(q)
    return ret

def puttingin(col, idx, isGaro, rev,s,dq):

    if not isGaro: #세로
        if rev: #거꾸로
            for i in range(2,-1,-1): cube[col][i][idx] = dq[s];s+=1
        else:
            for i in range(3): cube[col][i][idx] = dq[s];s+=1
    else: #가로
        if rev:
            for i in range(2,-1,-1):
                cube[col][idx][i] = dq[s];s+=1
        else:
            for i in range(3):cube[col][idx][i] = dq[s];s+=1

def putin(l,dq):
    start = 0
    for ll in l:
        puttingin(ll[0], ll[1], ll[2], ll[3],start,dq )
        start+=3

def rotateself(col, c):
    pre = deepcopy(cube[col])
    if c == "+": # 시계방향
        for y in range(3):
            for x in range(3):cube[col][x][abs(y-2)] = pre[y][x]
    else:
        for y in range(3):
            for x in range(3):
                cube[col][ abs(x-2) ][y] = pre[y][x]




for tt in range(t):
    n = int(input().rstrip())
    cube = [deque([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]), deque([['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]), deque([['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]), deque([['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]), deque([['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]), deque([['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']])]
    cmdd = input().split()
    for cm in cmdd:
        dq = reader(cm[0])
        dq.rotate( -3 if cm[1]=='-' else 3)

        putin(who[cm[0]],dq)
        rotateself(tonum[cm[0]],cm[1] )
    for i in cube[0]: print(*i, sep="")


