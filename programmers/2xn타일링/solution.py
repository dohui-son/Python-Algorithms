def solution(n):
    if n <= 3: return n
    memo = [i + 1 for i in range(n)]
    for i in range(2, n): memo[i] = (memo[i - 1] + memo[i - 2])% 1000000007
    return memo[n - 1]