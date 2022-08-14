def check(A, mcnt, msize):
    bsum, bcnt = 0, 0
    for a in A:
        if bsum+a > msize: 
            bsum = a
            bcnt += 1
        else: bsum += a
        if bcnt >= mcnt: return False
    return True


def solution(K, M, A):
    cnt = K
    low = max(A)
    up = sum(A)

    if cnt == 1: return up
    if cnt>=len(A): return low

    while low<=up:
        mid = (low+up)//2
        if check(A, cnt, mid) : up = mid-1
        else: low = mid+1
    return low