from collections import Counter
def solution(A):
    n = len(A)
    if n == 0: return -1
    if n == 1 : return 0
    arr = Counter(A).most_common()
    return A.index(arr[0][0]) if arr[0][1] > n//2 else -1 