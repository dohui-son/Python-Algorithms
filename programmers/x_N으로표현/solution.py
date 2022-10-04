def solution(N, number):
    if str(number) == str(N) * len(str(number)): return len(str(number))
    
    memo = [set() for _ in range(9)]
    for i in range(1, 9):
        memo[i].add(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            for a in memo[j]:
                for b in memo[i - j]:
                    memo[i].add(a - b)
                    memo[i].add(b - a)
                    memo[i].add(a + b)
                    memo[i].add(a * b)
                    if a > 0: memo[i].add(b // a)
                    if b > 0: memo[i].add(a // b)
        if number in memo[i]: return i
    return -1