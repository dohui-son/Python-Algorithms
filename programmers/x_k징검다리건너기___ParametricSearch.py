def check(k, num, st): # 징검다리 건너는 부분을 구현 못함
    cnt = 0
    for s in st:
        if s-num<=0: cnt+=1
        else: cnt = 0
        if cnt>=k: break
    return cnt>=k

def solution(stones, k):
    s, e = 0, 200000000
    while s+1<e:
        mid = (s+e)//2
        if check(k, mid, stones.copy()): e = mid
        else:s = mid

    return s+1