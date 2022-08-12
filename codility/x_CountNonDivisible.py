# 참고자료 : https://smecsm.tistory.com/235
from collections import Counter
def solution(A):
    N = len(A)
    dic = Counter(A)
    ans = [0]*N
    saved = [-1] * (2*N+1)
    for i in range(N):
        cur = A[i]
        if saved[cur] != -1: ans[i] = saved[cur]
        else :  
            count = 0
            for j in range(1, int(cur**0.5) + 1):
                if cur%j == 0:
                    count += dic[j]
                    if j != cur//j : count += dic[cur//j]
            ans[i] = N - count
            saved[cur] = ans[i]
    return ans