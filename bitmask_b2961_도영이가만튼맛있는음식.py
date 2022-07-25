import sys; from itertools import combinations
reader = sys.stdin.readline
n = int( reader().rstrip() ); arr = []; ans = int(1e9)
for i in range(n):
    s,ss = map(int,reader().split())
    arr.append([s,ss])
    if abs(s-ss) < ans : ans = abs(s-ss)
combi = []
for i in range(2,n+1):
    combi += list(combinations(arr,i))
for i in combi:
    s, ss = 1,0
    for j in i: 
        s*=j[0]; ss+=j[1]
    if ans > abs(s-ss): ans = abs(s-ss)
    if ans == 0: break
print(ans)