from collections import defaultdict
n,m = map(int, input().split())
tochr = ['']*n
tonum = defaultdict(str)
for i in range(n):
    st = input().rstrip()
    tochr[i] = st; tonum[st] = i+1
for i in range(m):
    st = input().rstrip()
    if ord( st[0] ) < 58: print( tochr[int(st)-1])
    else: print( tonum[st] )
#나는야포켓몬마스터이다솜
