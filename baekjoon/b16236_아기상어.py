# 24분 걸림
from collections import defaultdict, deque
global n,g,shy,shx,m,ans,cnt

ans,siz,cnt,m = 0,2,0,0
dir = [(-1,0),(0,-1),(0,1),(1,0)]
n = int(input().rstrip())
g = [[*map(int,input().split())] for _ in range(n)]
for y in range(n):
    for x in range(n):
        if g[y][x]!=9 and g[y][x]!=0: m+=1
        elif g[y][x] == 9: shy = y; shx = x; g[y][x] = 0



def eat():
    global n,g,shy,shx,m,ans,cnt
    q = deque([(shy,shx)])
    visit = [[0]*n for _ in range(n)]
    visit[shy][shx] = 1
    hoobo = []
    flag = False
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny>=0 and nx>=0 and ny<n and nx<n:
                if visit[ny][nx] or g[ny][nx]>siz : continue
                visit[ny][nx] = visit[y][x]+1
                if g[ny][nx] and g[ny][nx]<siz:
                    if hoobo:
                        if hoobo[-1][0]>=visit[y][x] : hoobo.append((visit[y][x],ny,nx))
                        else: flag = True; break
                    else: hoobo.append((visit[y][x],ny,nx))
                q.append((ny,nx))
        if flag: break
    if hoobo: 
        hoobo.sort()
        t,y,x = hoobo[0]
        ans+=t; g[y][x] = 0; shy,shx = y,x
        return True
    else: return False

for _ in range(m):
    if eat()==False: break
    else: cnt+=1
    if cnt == siz : siz+=1; cnt = 0
print(ans)



# bfs 문제( heap을 이용해도 좋을 것 같다. )
# (1) bfs를 하면서 그 다음 잡아먹을 수 있는 물고기들을 array에 (이동칸수, 물고기 y 좌표, 물고기 x 좌표) 형태로 저장해준다.
# (2) bfs 도중 - 잡아먹을 수 있는 물고기를 저장해줄때마다 "잡아먹을 수 있는 물고기들을 저장해둔 array"의 마지막 원소의 이동칸수보다 현재 잡아먹을 수 있는 물고기까지의 이동칸수를 확인해준다. 만약 저장해둔 마지막 원소의 이동칸수보다 현재 잡아먹을 수 있는 물고기까지의 이동칸수가 더 크면 BFS 탐색을 멈춘다.
# (3) bfs 탐색이 끝났을 때 잡아먹을 수 있는 물고기 정보를 저장해둔 array가 NULL이면, 아기상어는 엄마를 찾으러 간다
# (4) bfs 탐색이 끝났을 때 잡아먹을 수 있는 물고기 정보를 저장해둔 array가 비어있지 않다면, sort를 해준 후, 가장 첫번째 원소의 물고기 정보를 이용해서 물고기를 죽이고, 이동시간을 더해준 다음, 상어의 위치를 갱신해준다.