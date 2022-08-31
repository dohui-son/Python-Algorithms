import sys; reader = sys.stdin.readline
from collections import defaultdict,deque
from sys import setrecursionlimit
setrecursionlimit(5000)
INF = int(2e9)

aord = ord('A'); tonum = defaultdict(int); tonum[(1<<0)] = 0; tonum[(1<<1)] = 1; tonum[(1<<2)] = 2; tonum[(1<<3)] = 3
block = defaultdict(int)
block[0] = 3; block[1] = 0; block[2] = 1; block[3] = 2

n = int(reader().rstrip())
INF = 0
car = [deque([]) for _ in range(4)]

all = 0
for nn in range(n):
    time, w = input().split()
    time = int(time)
    car[ord(w) - aord].append( [time,nn] )
    all +=1
    INF = max( INF, time+1)


ans = [-1] * n

pre = -1
while all>0:
    # 차량 하나 나갈때마다 all 개수 하나씩 없애기
    nowbit, nowtime,cnt = 0, INF, 0 # nowtime이 바뀌어서 수정 필요
    flag = False 
    for i in range(4):
        if car[i] :
            if pre+1 >= car[i][0][0]: # 지금 시점에 바로 갈 수 있는 애들
                if flag: 
                    nowbit |= (1<<i)
                    cnt +=1
                else: 
                    nowbit = (1<<i)
                    cnt = 1; 
                    nowtime = pre+1
                    flag = True
            else: # 지금 시간 이후로 도착한 애들 - 지금 이후로 도착하는 애들끼로 고르려면 가장 빨리 도착하는 애를 골라야함
                if flag: continue
                if nowtime > car[i][0][0]:
                    nowbit = (1<<i)
                    nowtime = car[i][0][0]
                    cnt = 1
                elif nowtime == car[i][0][0]: 
                    nowbit |= (1<<i)
                    cnt += 1 

    if cnt == 4:break 
    bit = nowbit
    while bit:
        nextt = bit&-bit
        bit &= (bit-1)
        num = tonum[nextt]
        if nowbit & (1<<block[num]): continue
        ans[ car[num][0][1] ] = nowtime
        all -= 1
        car[num].popleft()     
        
    pre = nowtime
    

print(*ans, sep="\n")