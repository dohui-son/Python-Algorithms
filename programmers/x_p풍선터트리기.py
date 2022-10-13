def solution(a):
    ans, n = 0, len(a)
    INF = 1000000000
    mini = [[0,0] for i in range(n)]
    mini[0][0], mini[n-1][1] = a[0], a[n-1]
    for i in range(0, n): 
        if i > 0: mini[i][0] = min(mini[i-1][0], a[i])
        j = n-i-1
        if j < n-1: mini[j][1] = min(mini[j+1][1], a[j])
    for i in range(1, n-1):
        if mini[i-1][0] > a[i] or mini[i+1][1] > a[i]: ans += 1
    return ans+2