from sys import stdin

h, w = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(h)]

def move(x,y,dx, dy):
    cnt = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return y,x,cnt

def sol():
    visited = {}
    for y, b in enumerate(board):
        for x, r in enumerate(b):
            if r == 'R':
                r_x, r_y = x,y
            if r == 'B':
                b_x, b_y = x,y
    n_list = [[r_x, r_y, b_x, b_y, 1]]
    visited[(r_x, r_y, b_x, b_y)] = 1
    d_ = [[0,1], [0,-1], [-1,0], [1,0]]
    while n_list:
        now = n_list.pop(0)
        rx, ry, bx, by = now[0], now[1], now[2], now[3]
        if now [4] > 10:
            break
        for d in d_:
            rty, rtx, rcnt = move(rx, ry, d[0], d[1])
            bty, btx, bcnt = move(bx, by, d[0], d[1])
            if board[bty][btx] != 'O':
                if board[rty][rtx] == 'O':
                    print(now[4])
                    return
                if btx == rtx and bty == btx:
                    if rcnt > bcnt:
                        rtx -= d[0]
                        rty -= d[1]
                    else:
                        btx -= d[0]
                        bty -= d[1]
                if (rtx, rty, btx, bty) in visited:
                    continue
                visited[(rtx, rty, btx, bty)] = 1
                n_list.append([rtx, rty, btx, bty, now[4]+1])
    print(-1)

sol()