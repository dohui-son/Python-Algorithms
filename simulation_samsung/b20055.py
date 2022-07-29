import sys; from collections import defaultdict,deque
reader = sys.stdin.readline

dic = defaultdict(int)
n, k = map(int, reader().split())
l = list(map(int, reader().split()))
for i in range(2*n): dic[i] = l[i]
up = 0; down = n-1;zero = 0; dq = deque( [] ); ans = 0;visit = [False]*(2*n)
def findN(now):
    if now-1<0: return 2*n-1
    return now-1

while zero < k:
    up = findN(up); down = findN(down)
    if down in dq: visit[down] = False; dq.remove(down) #내리기
    if dq:
        dlen = len(dq)
        for i in range(dlen):
            now = dq.popleft()
            ne = (now+1)%(2*n)
            if visit[ne] == True or dic[ne] <= 0 : dq.append(now)
            elif dic[ne] > 0 :
                visit[now] = False
                dic[ne] -= 1
                if dic[ne] == 0 : zero+=1
                if ne != down:
                    dq.append(ne); visit[ne] = True
    if dic[up]>0 : # 3 번
        dic[up]-=1
        dq.append(up); visit[up] = True
        if dic[up] == 0: zero+=1
    ans+=1
    if zero>=k: print(ans); break