from collections import defaultdict, deque
global ans,rscore, n
ans = [-1]
rscore, n = 0 , 0
def BT( info, rest, rec, start):
    global ans,rscore, n

    if ( rest ==0 or start==10 ) : 
        ap, score = 0, 0
        mini = [0]*11
        for i in range(10):
            if info[i] == 0 and rec[i] == 0: continue
            if info[i] >= rec[i]: ap += (10-i)
            else: score += (10-i) 

        if score > ap and score-ap >rscore:
            ans = rec.copy(); 
            rscore = score-ap
            if rest : ans[-1] = rest
        elif score > ap and score-ap  == rscore:
            pre, now = 0,0

            for i in range(9,0,-1):
                if pre > now or pre<now: break
                if rec[i]>0: now += rec[i]
                if ans[i]>0: pre += ans[i]
            if pre<now: 
                ans = rec.copy(); 
                rscore = score-ap
                if rest : ans[-1] = rest

        return
    else : 
        for i in range(start, 11):
            if rest > info[i]:
                pre = rec[i]
                rec[i] = info[i]+1 
                BT(info, rest-rec[i], rec, i+1 )
                rec[i] = pre
            else: BT(info, rest, rec, i+1 )

def solution(N, info):
    global ans,rscore,n
    rec = [0]*11
    n = N
    nn = N
    BT(info, nn, rec, 0  )

    return ans 