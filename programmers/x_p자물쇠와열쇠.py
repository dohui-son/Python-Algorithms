from copy import deepcopy

def rotation(key, m):
    pre = deepcopy(key)
    for y in range(m):
        for x in range(m): key[x][m - 1 - y] = pre[y][x]

def solution(key, lock):
    ans, n, m, zero = len(lock), len(key), 0
    for i in lock: zero += i.count(0)
    
    for i in range(6):
        for py in range(-19, 20):
            for px in range(-19, 20):
                flag, cnt = True, 0
                for y in range(m):
                    for x in range(m):
                        ny = y + py
                        nx = x + px
                        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
                        if lock[ny][nx] == 1 and key[y][x]: flag = False
                        elif lock[ny][nx] == 0 and key[y][x]: cnt += 1
                if flag and cnt == zero: return True
        rotation(key, m)
    return False