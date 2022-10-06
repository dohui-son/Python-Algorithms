from collections import defaultdict, deque
import heapq as hq

def solution(board, nums):
    ans = 0
    where = defaultdict(int)
    n = len(board)
    v = [[0]*n for _ in range(n)]
    
    for y in range(n):
        for x in range(n): where[board[y][x]] = (y, x) 
    for num in nums:
        y, x = where[num]
        v[y][x] = 1
    col = [[0]*n for _ in range(n)]
    diag = [[0]*n for _ in range(n)]
    for y in range(n):
        if sum(v[y]) == n: ans += 1
        for x in range(n):
            col[x][y] = v[y][x]
            if y == x: diag[0][y] = v[y][x]
            if y + x == n - 1: diag[1][y] = v[y][x]
    if sum(diag[0]) == n: ans += 1
    if sum(diag[1]) == n: ans += 1
    for i in range(n): 
        if sum(col[i]) == n: ans += 1
    
    return ans