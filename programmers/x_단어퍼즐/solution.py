def solution(strs, t):
    INF = int(3e9)
    memo = [INF] * (len(t) + 1)
    memo[0] = 0
    for i in range(1, len(t) + 1):
        j = 0 if i - 5 < 0 else i - 5
        while j < i:
            if t[j:i] in strs and memo[j] + 1 < memo[i]: memo[i] = memo[j] + 1
            j += 1
    return memo[len(t)] if memo[len(t)] != INF else -1 