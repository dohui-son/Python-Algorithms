from collections import defaultdict, deque; from itertools import combinations
# 1시간 45분 치킨거리 
# 코드 최적화 가능
n,m = map(int,input().split()); ans = int(2e9)
g = [ list( map(int,input().split()) ) for _ in range(n)]
chi = deque(); home = deque(); h_chi = []
for i,ival in enumerate(g):
    for j, val in enumerate(ival):
        if val == 1: home.append((i,j))
        elif val == 2: chi.append((i,j))
clen =  len(chi); hlen = len(home)
h_chi = [ [] for _ in range(hlen)]
for cdx,c in enumerate(chi):
    cy, cx = c
    for hdx, h in enumerate(home):
        hy,hx = h
        cal = abs(cy-hy)+abs(cx-hx)
        h_chi[hdx].append( (cal, cdx) )
for h in h_chi: h.sort()
arr = [i for i in range(clen)]

combi = list( combinations(arr,m) )
for c in combi:
    summ = 0

    for h in h_chi:
        for hh in h:
            cal,cdx = hh
            if cdx in c: summ+= cal;break
    ans = min(ans, summ)
print(ans)
