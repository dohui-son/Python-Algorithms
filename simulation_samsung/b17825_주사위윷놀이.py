# 1시간 3분
from collections import defaultdict,deque
global go,score,dice,ans

ans = 0
go = [[1], [2],[3],[4],[5],[6,26],[7],[8],[9],[10],[11,21],[12],[13],[14],[15],[16,29],[17],[18],[19],[20],[-1],[22],[23],[24],[25],[20],[27],[28],[23],[30],[31],[23] ]
#for i,val in enumerate(go): print(i, val)
score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,22,24,25,30,35,13,16,19,28,27,26]
# for i, val in enumerate(score): print(i,val)
mal = [0]*4
dice = [*map(int,input().split())]

def bt(idx, nscore):
    global go, score, dice, ans
    if idx == 10: ans = max(ans,nscore); return
    #if idx == 3: print(dice[idx], mal, nscore)
    kan = dice[idx]
    for m in range(4):
        if mal[m] == -1: continue
        pos = mal[m]

        if len( go[pos] ) == 2:  pos = go[pos][1]
        else:  pos = go[pos][0]
        if pos>-1:
            for _ in range(kan-1) :
                pos = go[pos][0]
                if pos == -1: break
        if pos>-1 and pos in mal: continue
        else:
            pre = mal[m]
            mal[m] = pos
            if pos == -1: bt(idx+1,nscore)
            else:bt(idx+1,nscore+score[pos])
            mal[m] = pre
bt(0,0)
print(ans)