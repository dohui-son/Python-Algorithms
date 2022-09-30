N, M = map(int, input().split())
Map = [ list(map(int, input().split())) for _ in range(N) ]
magic = [ list(map(int, input().split())) for _ in range(M) ]

direct_cnt = [ i//2 for i in range(2, N*2) ]
direct_cnt.append(N-1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cur_list = [0] * (N*N)
cnt = 1; x, y = N//2, N//2; d=0

marvel_cnt = [0] * 4

for dc in direct_cnt:
    for i in range(dc):
        x, y = x+dx[d], y+dy[d]
        cur_list[cnt] = Map[y][x]
        cnt += 1
    d = (d+1)%4

def move_marvel():
    new_list = [0] * (N*N)
    cnt = 1
    for i in range(1, N*N):
        if cur_list[i]:
            new_list[cnt] = cur_list[i]
            cnt += 1
    return new_list

def explosion():
    flag = 0; start = 1; end = 2
    while(start < N*N and end < N*N):
        if cur_list[start] != cur_list[end]:
            if (end - start) > 3:
                for i in range(start, end):
                    flag = 1
                    marvel_cnt[cur_list[start]] += end - start
                    cur_list[i] = 0
            start = end
            end = start + 1
        else:
            end += 1
    return flag

def change_list():
    new_list = [0] * (N*N)
    start = 1; end = 2; cnt = 1
    while ( start < N*N  and end < N*N and cnt < N*N):
        if cur_list[start] != cur_list[end]:
            new_list[cnt] = end-start
            new_list[cnt + 1] = cur_list[start]
            cnt += 2
            start = end
            end = start + 1
        else:
            end += 1
    return new_list

plus = 2
ice_break_idx = [0] * (N//2)*4
ice_break_idx[0] = 1
for i in range(1, (N//2)*4):
    ice_break_idx[i] = ice_break_idx[i-1] + plus
    if i%4 == 0 or i%4 == 3:
        plus += 1

d_map = [0, 3, 1, 0, 2 ]
for d, s in magic:
    d = d_map[d]
    cnt = 0
    for i in range(0, (N//2)*4):
        if cnt >= s:
            break
        if (i%4) == d:
            cur_list[ice_break_idx[i]] = 0
            cnt += 1
    cur_list = move_marvel()
    while (explosion()):
        cur_list = move_marvel()
    cur_list = change_list()

print(marvel_cnt[1]+2*marvel_cnt[2]+3*marvel_cnt[3])