global ans
ans = []

def hannoi(n, fromm, to):
    if n == 0: return
    mid = 6 - fromm - to
    hannoi(n - 1, fromm, mid)
    ans.append((fromm, to))
    hannoi(n - 1, mid, to)
    
def solution(n):
    global ans
    hannoi(n, 1, 3)
    return ans