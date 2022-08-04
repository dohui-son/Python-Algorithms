from collections import defaultdict,deque
import sys; reader = sys.stdin.readline
msg = reader().rstrip()
keyy = reader().rstrip()
dic = defaultdict(list)

visit = [False]*26
#첫 번째 줄에 Playfair cipher로 암호화된 결과를 출력한다.
g = [['']*5 for _ in range(5)]
yy = 0;xx = 0;tmp = 0
for i in keyy:
    if visit[ord(i)-ord('A')]: continue
    if xx == 5: yy+=1; xx = 0
    g[yy][xx] = i
    dic[i] = [yy,xx]
    visit[ord(i)-ord('A')] = True
    xx+=1
    tmp += 1
if tmp < 25:
    for i in range(26):
        if i == ord('J')-ord('A'):continue
        if visit[i] == False:
            if xx == 5: yy+=1; xx = 0
            g[yy][xx] = chr( i+ord('A') )
            dic[ g[yy][xx] ] = [yy,xx]
            xx+=1
msgl = []; mlen = len(msg)
mlen = len( msg )
dq = deque(); msg2 = ''
for i in msg: dq.append(i)
while dq:
    a = dq.popleft()
    if dq:
        if dq[0] == a:
            if a == 'X': msg2 += (a + 'Q') 
            else:  msg2 += (a + 'X') 
        else:
            b = dq.popleft()
            msg2 += (a+b)
    else: #마지막 하나 남은게 한개인 경우 
        msg2 += ( a + 'X')
mlen = len(msg2); ans = ''
for i in range(0, mlen-1, 2):
    y,x = dic[ msg2[i] ]
    yy, xx = dic[ msg2[i+1] ]
    if y == yy: #1번 조건
        x = (x+1)%5
        xx = (xx+1)%5
        ans += g[y][x]
        ans += g[yy][xx]
    elif x == xx:
        y = (y+1)%5
        yy = (yy+1)%5
        ans += g[y][x]
        ans += g[yy][xx]
    else:
        ans += g[y][xx]
        ans += g[yy][x]
print(ans)









