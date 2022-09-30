dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
sdx = [0, -1, 0, 1]
sdy = [-1, 0, 1, 0]
dic = [(i,j,k) for i in range(4) for j in range(4) for k in range(4)]
M, S = map(int, input().split())
fish = [[[0]*8 for _ in range(4)] for _ in range(4)]
for _ in range(M):
  y, x, d = map(int,input().split())
  fish[y-1][x-1][d-1] += 1

sy, sx = map(int, input().split())
sy -= 1
sx -= 1

smell = [[0]*4 for _ in range(4)]

for _ in range(S):
  next_fish = [[[] for _ in range(4)] for _ in range(4)]
  moved_fish = [[[0]*8 for _ in range(4)] for _ in range(4)]

  # 물고기 복제해두기
  for i in range(4):
    for j in range(4):
      next_fish[i][j] = fish[i][j][:]
  
  # 물고기 이동
  for i in range(4):
    for j in range(4):
      for k in range(8):
        if fish[i][j][k] > 0 :
          y, x, d = i, j, k
          for l in range(8) :
            nd = (d-l)%8
            ax, ay = x+dx[nd], y+dy[nd]
            if -1<ax<4 and -1<ay<4 and smell[ay][ax] == 0 and (sx,sy) != (ax,ay) :
              x, y, d = ax, ay, nd
              break
          moved_fish[y][x][d] += fish[i][j][k]
  max_cnt, max_move = -1, -1
  for i in dic :
    ax, ay = sx, sy
    tmp = set([])
    flg = False
    for j in i :
      ax, ay = ax+sdx[j], ay+sdy[j]
      if not (-1<ax<4 and -1<ay<4) :
        flg = True
        break
      tmp.add((ax, ay, sum(moved_fish[ay][ax])))
    if flg : continue
    if max_cnt < sum([x[-1] for x in tmp]):
      max_cnt, max_move = sum([x[-1] for x in tmp]), i
  for i in max_move :
    sx, sy = sx+sdx[i], sy+sdy[i]
    if  sum(moved_fish[sy][sx]) > 0:
      smell[sy][sx] = 3
      moved_fish[sy][sx] = [0]*8
  for i in range(4):
    for j in range(4):
      smell[i][j] = max(smell[i][j]-1, 0)
      for k in range(8):
        moved_fish[i][j][k] += next_fish[i][j][k]
  fish = moved_fish
ans = 0
for i in fish:
  for j in i:
    ans += sum(j)
print(ans)