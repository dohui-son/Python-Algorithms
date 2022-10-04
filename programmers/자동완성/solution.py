def solution(words):
    ans, n = 0, len(words)
    words.sort()
    simil = [[0, 0] for _ in range(n)]
    for i in range(n - 1):
        if i > 0: simil[i][0] = simil[i-1][1]
        for j in range(len(words[i])):
            if j >= len(words[i + 1]): break
            if words[i][j] == words[i+1][j]: simil[i][1] += 1
            else: break
        ans += (max(simil[i]) if max(simil[i]) == len(words[i]) else max(simil[i]) + 1)
    ans += (simil[n-2][1] if simil[n-2][1] == len(words[-1]) else simil[n-2][1] + 1)
    return ans