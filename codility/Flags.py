def check(k):
    global plen,dis
    nowk = 1
    i , summ = 0,0
    while i < plen:
        while i < plen and summ < k:
            summ += dis[i]
            i+=1
        if summ >=k: nowk += 1; summ = 0
        if nowk >= k: return nowk
    return nowk

def solution(A):
    n = len(A)
    global plen, dis
    peak = [0]*n; plen = 0
    dis = [0]*n ; cnt = 1
    for i in range(1,n-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peak[plen] = i; dis[plen] = cnt; 
            cnt = 1;plen += 1
        else: cnt+=1
    dis[0] = 0
    if plen <= 1: return plen
    if plen == 2 : return 2 if dis[1]-dis[0]>=2 else 1
    s = -1; e = plen+1
    while (s+1<e):
        mid = (s+e)//2
        res = check(mid)
        if res >= mid: s = mid
        else: e = mid
    return s