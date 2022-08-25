from collections import deque, defaultdict

n = int(input().rstrip())
g = [ [*map(int, input().split())] for _ in range(n) ]
ty,tx = (n-1)//2, (n-1)//2
mdir = defaultdict(list)
# 좌0 하1 우2 상3
dir = [ (0,-1 ), (1,0), (0,1), (-1,0) ]

mdir[0] = [(-1,1),(1,1),  (-2,0),(2,0),    (0,-2),  (-1,0),(1,0) ,   (-1,-1),(1,-1)] #
mdir[1] = [(-1,-1),(-1,1)  ,(0,-2),(0,2),   (2,0),  (0,-1),(0,1),     (1,-1),(1,1)]  #
mdir[2] = [(-1,-1),(1,-1),  (2,0),(-2,0)  ,  (0,2),   (-1,0),(1,0),   (-1,1),(1,1)]  #
mdir[3] = [(1,-1),(1,1),     (0,-2),(0,2),   (-2,0)   ,(0,1),(0,-1),    (-1,-1),(-1,1) ] #
percent = [1,1,            2,2,              5,       7,7,            10,10]
ans = 0

for circle in range(n//2+1):
    for dx, d in enumerate(dir):
        if circle == n // 2 and dx == 1: break  # 마지막 회차에서는 0번방향만 하고 끝남

        go = 0 # 해당방향으로 몇칸 갈지
        if dx<=1: go = circle*2 + 1
        else : go = (circle+1) * 2

        while go:

            fy, fx = ty+d[0] ,tx+d[1] #토네이도 바로 옆동 - 모레 제공하는 곳
            ry, rx = fy+d[0] ,fx+d[1] #남은 모레가 갈 동좌표


            ty, tx = d[0] + ty, d[1] + tx  # 토네이도 한칸 이동
            go -= 1

            if fy<0 or fx<0 or fy>=n or fx>=n: continue
            rest = g[fy][fx]


            for dd in range(9):
                ny,nx = fy+mdir[dx][dd][0], fx+mdir[dx][dd][1]
                morae = g[fy][fx]*percent[dd]//100
                if morae > 0:
                    rest -= morae
                    if ny<0 or nx<0 or ny>=n or nx>=n : ans += morae
                    else: g[ny][nx] += morae
            if rest>0:
                if ry<0 or rx<0 or ry>=n or rx>=n : ans += rest #남은 모레 옮겨주기
                else: g[ry][rx] += rest
            g[fy][fx] = 0

print(ans)