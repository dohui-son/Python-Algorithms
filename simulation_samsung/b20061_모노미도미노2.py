#모노미노도미노2 - 1시간 31분
from collections import deque,defaultdict

global n,gr,bl,ans

ans = 0
n = int(input().rstrip())


gr = deque([[0]*4 for _ in range(6)])
bl = deque([[0]*4 for _ in range(6)])

def delbase(g,many):
    for i in range(many):
        del g[-1]
        g.appendleft([0]*4)

# 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동
#행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
# 이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리


def green(t,bx):
    global n, gr, bl, ans

    sy = 0
    for yy in range(0,6):
    # 쌓을 위치 찾기
        if t == 1 and gr[yy][bx] == 0 : sy = yy
        if t == 2 and gr[yy][bx] == 0 and gr[yy][bx+1] == 0: sy = yy
        if t == 3 and yy==5: break
        if t == 3 and gr[yy][bx] == 0 and gr[yy+1][bx] == 0: sy = yy
        if t == 1 and gr[yy][bx] != 0: break
        if t == 2 and ( gr[yy][bx] != 0 or gr[yy][bx+1] != 0): break
        if t == 3 and (gr[yy][bx] != 0 or gr[yy+1][bx] != 0): break



    # 블럭 쌓기
    gr[sy][bx] = 1
    if t == 2 : gr[sy][bx+1] = 1
    elif t ==3: gr[sy+1][bx] = 1

    # 점수 확인해주기
    if sy >= 2:
        if sum(gr[sy]) == 4:
            ans += 1
            del gr[sy]
            gr.appendleft([0]*4)

    if t==3 and sy+1>=2:
        if sum(gr[sy+1]) == 4:
            ans += 1
            del gr[sy+1]
            gr.appendleft([0]*4)


    # 0,2번째줄 있나 확인해서 바닥줄 없애주기
    if 1 in gr[0]:delbase(gr,2)
    elif 1 in gr[1]: delbase(gr,1)

def blue(t,bx):
    global n, gr, bl, ans

    sy = 0
    for yy in range(0, 6):
        # 쌓을 위치 찾기
        if t == 1 and bl[yy][bx] == 0: sy = yy
        if t == 3 and bl[yy][bx] == 0 and bl[yy][bx + 1] == 0: sy = yy

        if t == 2 and yy == 5: break
        if t == 2 and bl[yy][bx] == 0 and bl[yy + 1][bx] == 0: sy = yy

        if t == 1 and bl[yy][bx] != 0: break
        if t == 3 and (bl[yy][bx] != 0 or bl[yy][bx + 1] != 0): break
        if t == 2 and (bl[yy][bx] != 0 or bl[yy + 1][bx] != 0): break

    # 블럭 쌓기
    bl[sy][bx] = 1
    if t == 3:
        bl[sy][bx + 1] = 1
    elif t == 2:
        bl[sy + 1][bx] = 1

    # 점수 확인해주기
    if sy>=2:
        if sum(bl[sy]) == 4:
            ans += 1
            del bl[sy]
            bl.appendleft([0] * 4)

    if t == 2 and sy+1>=2 :
        if sum(bl[sy + 1]) == 4:
            ans += 1
            del bl[sy+1]
            bl.appendleft([0] * 4)


    # 0,2번째줄 있나 확인해서 바닥줄 없애주기
    if 1 in bl[0]:
        if t == 2 and sy == 0:delbase(bl, 2)
    elif 1 in bl[1]:delbase(bl, 1)


summ = 0
for _ in range(n):
    t, y, x = map(int,input().split())
    green(t,x)
    blue(t,y)
    # print(t,y,x)
    # for i in gr: print(i)
print(ans)
for i in range(2,6):
    summ +=(sum(gr[i])+sum(bl[i]))
print(summ)
