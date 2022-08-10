from collections import deque
def solution(A, K):
    if K == 0 or len(A) == 0: return A
    if min(A) == max(A): return A
    n = len(A)
    k = K%n
    if k == 0: return A
    a = deque(A)
    a.rotate(k)
    return list(a)