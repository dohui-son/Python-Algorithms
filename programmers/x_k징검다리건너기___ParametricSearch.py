def check(k, num, st): # check(징검다리 해당 인원만큼 건널 수 있는지 확인하는 함수) 를 제대로 완성하기 못함
    cnt = 0
    for s in st:
        if s-num<=0: cnt+=1
        else: cnt = 0
        if cnt>=k: return False # cnt>k가 아닌 이유 : 네 번째 친구가 징검다리를 건너려면, 3 번째 디딤돌에서 7 번째 디딤돌로 네 칸을 건너뛰어야 합니다. 하지만 k = 3 이므로 건너뛸 수 없습니다.
    return True

def solution(stones, k):
    s, e = 1, 200000000
    while s+1<e:
        mid = (s+e)//2
        if check(k, mid, stones): s = mid
        else:e = mid

    return s+1 # s+1 임을 유의할 것
