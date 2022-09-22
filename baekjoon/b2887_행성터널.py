from collections import defaultdict,deque
import sys
input = sys.stdin.readline
n = int(input().rstrip())

parent = [i for i in range(n)]
x , y, z = [], [], []
for i in range(n):
    a,b,c = map(int ,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

# (1) 가중치 (후보들) 직접 구하는 연산
x.sort()
y.sort()
z.sort()
e = []
for l in x,y,z:
    for i in range(0,n-1):
        e.append( (abs(l[i][0]-l[i+1][0]), l[i][1], l[i+1][1]) )


# (2) fundamental한 크루스칼 알고리즘 동작
def findd(x):
    if x != parent[x]: parent[x] = findd( parent[x] )
    return parent[x]

def union(a,b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return False
    if aa < bb: parent[bb] = aa
    else: parent[aa] = bb
    return True

e.sort() # 크루스칼 알고리즘에서 중요한 가중치 소팅 - greedy한 크루스칼 알고리즘이라고 할 수 있다.
ans, cnt = 0, 0
for l in e:
    cost, a,b = l
    if union(a,b): ans += cost; cnt+=1
    if cnt == n-1: break
print(ans)