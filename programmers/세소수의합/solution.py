from bisect import bisect_left

def solution(n):
    ans = 0
    if n <= 3: return 0
    
    p = [0, 0] + [1] * ~-n
    for i in range(int(n ** .5) + 1):
        if p[i]: p[i * i::i] = [0] * (n // i - i + 1)
    p = [2] + [i for i in range(3, n + 1, 2) if p[i]]
    
    idx = bisect_left(p, n)
    if idx >= len(p): idx -= 1
    for a in range(idx, 1, -1):
        aa = n - p[a]
        if aa <= 0 : continue
        for b in range(a-1, 0, -1):
            if aa - p[b] <= 0: continue
            if aa - p[b] != p[b] and aa - p[b] != p[a] and aa - p[b] < p[a] and aa - p[b] < p[b] and  aa - p[b] in p: 
                ans += 1
    return ans