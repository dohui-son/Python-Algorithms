import sys; from itertools import combinations
reader = sys.stdin.readline
n,k = map(int,reader().split())
basic = {'a','n','t','i','c'}
arr = [] ; hoobo = set(); ans = 0
for i in range(n):
    se = set( reader().rstrip()[4:-4] )
    hoobo |= se
    arr.append(se)
if k<5: print(0); exit(0)
if k == 26: print(n); exit(0)
hoobo -= basic
combi = combinations(hoobo, min(k-5, len(hoobo))) #유의
for w in combi:
    word = set(w) | basic
    cnt = 0
    for i in arr:
        if i <= word: cnt += 1 # i가 word의 부분집합인지 확인할때 <=를 쓰면 됨
    if cnt > ans: ans = cnt
print(ans)