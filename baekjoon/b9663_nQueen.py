from multiprocessing.connection import answer_challenge
import sys; sys.setrecursionlimit(7000); input = sys.stdin.readline
from collections import defaultdict,deque
global n,ans
ans = 0
tonum = defaultdict(int)

def NQueen(y, ld, rd, n):
    total = (1 << n) - 1
    if total == y: return 1
    cnt = 0
    bit = ~(y | ld | rd) & total
    while bit:
        nextt = bit & -bit
        bit -= nextt
        cnt += NQueen(y | nextt, (ld | nextt) >> 1, (rd | nextt) << 1, n)
    return cnt

n = int( input().rstrip() )

print(NQueen(0, 0, 0, n))