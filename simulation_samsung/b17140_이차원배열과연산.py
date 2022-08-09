#이차원배열과 연산
#2시간 8분
from collections import deque, defaultdict
ans = int(1e9)
yul = 3; hang = 3
r,c,k = map( int, input().split() )
arr = [ list(map(int,input().split())) for _ in range(3)]
ga = [[-1]*100 for _ in range(100)]
se = [[-1]*100 for _ in range(100)]

for i in range(3):
    for j in range(3):
        ga[i][j] = arr[i][j]
        se[j][i] = arr[i][j]
for t in range(0,101):
    if ga[r-1][c-1] == k: ans = t; break
    if hang < yul:
        newhang = 0; yul=0
        for i in range(100):
            visit = 0
            tmp = []
            se[i].sort(reverse=True)
            notzero = 100; now = 0
            if -1 in se[i]: notzero -= se[i].count(-1)
            if notzero :
                yul += 1
                for j in range(100):
                    if se[i][j] == -1 : break
                    if now == notzero: break
                    if (1<<se[i][j]) & visit: continue
                    else:
                        cnt = se[i].count(se[i][j])
                        now += cnt
                        tmp.append( (cnt,se[i][j]) )
                        visit |= (1<< se[i][j])
                tmp.sort()
            tmplen = len(tmp)
            newhang = max(newhang, (tmplen*2)%101)
            if tmplen > 50 : tmplen = 50
            j = 0; idx = 0
            while j < 100:
                if idx == tmplen:
                    se[i][j] = -1; ga[j][i] = -1
                else:
                    se[i][j] = tmp[idx][1]
                    ga[j][i] = tmp[idx][1]
                    if j + 1 >= 100: break
                    j += 1
                    se[i][j] = tmp[idx][0]
                    ga[j][i] = tmp[idx][0]
                    idx += 1
                j += 1
        hang = newhang

    else:
        newyul = 0; hang = 0
        for i in range(100):
            visit = 0; tmp = []
            ga[i].sort(reverse=True)
            notzero = 100 ; now = 0
            if -1 in ga[i]: notzero -= ga[i].count(-1)
            if notzero :
                hang+=1
                for j in range(100):
                    if ga[i][j] == -1: break
                    if now == notzero: break
                    if (1 << ga[i][j]) & visit: continue
                    else:
                        cnt = ga[i].count(ga[i][j])
                        now += cnt
                        tmp.append( (cnt,  ga[i][j]) )
                        visit |= (1 << ga[i][j])
                tmp.sort()
            tmplen = len(tmp)
            newyul = max( newyul,  (tmplen*2)%101 )
            if tmplen>50: tmplen = 50
            j = 0; idx = 0
            while j < 100:
                if idx == tmplen: ga[i][j] = -1; se[j][i] = -1
                else:
                    ga[i][j] = tmp[idx][1]
                    se[j][i] = tmp[idx][1]
                    if j+1>=100:break
                    j+=1
                    ga[i][j] = tmp[idx][0]
                    se[j][i] = tmp[idx][0]
                    idx += 1
                j += 1

        yul = newyul
print(-1) if ans == int(1e9) else print(ans)