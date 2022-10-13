from collections import defaultdict, deque

n, m = map(int ,input().split())
bigger = [ set() for _ in range(n)]
smaller = [ set() for _ in range(n)]
for _ in range(m):
    small, big = map(int ,input().split())
    bigger[small-1].add(big-1)
    smaller[big-1].add(small-1)
ans = 0
for i in range(n): 
    se = bigger[i] | smaller[i] 
    se.add(i)
    for b in bigger[i]: se |= bigger[b]
    for s in smaller[i]: se |= smaller[s]
    if len(se) == n: ans += 1
print(ans)