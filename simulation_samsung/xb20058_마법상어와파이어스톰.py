import sys
input = sys.stdin.readline

N,Q = map(int, input().split())
TN=2**N
A=[list(map(int, input().split())) for _ in range(TN)]
visited=[[False]*(TN) for _ in range(TN)]
L=list(map(int, input().split()))

def rotate(A, l):
    Tl=2**l
    B=[[] for _ in range(TN)]
    for k in range(TN // Tl):
        for x in range(0,TN, Tl):
            temp = []
            for y in range(k*Tl, (k+1)*Tl) : temp.append(A[y][x:x+Tl])
            temp = [list(reversed(t)) for t in zip(*temp)]
            for i in range((k+1)*Tl-1, k*Tl-1, -1): B[i] += temp.pop()
    return B

def melt(A):
    temp=[a[:] for a in A]
    for i in range(TN):
        for j in range(TN):
            if not A[i][j]: continue
            count=4
            if i+1>=TN or A[i+1][j]==0: count-=1
            if i-1<0 or A[i-1][j]==0: count-=1
            if j+1>=TN or A[i][j+1]==0: count-=1
            if j-1<0 or A[i][j-1]==0: count-=1
            if count<3: temp[i][j]-=1
    return temp

def dfs(start):
    global count
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while start:
        x,y=start.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=TN or ny<0 or ny>=TN or A[nx][ny]==0 or visited[nx][ny]==True: continue
            visited[nx][ny]=True
            count+=1
            start.append([nx,ny])

for l in L:
    if l: A=rotate(A,l)
    A=melt(A)

ans1=0
ans2=0
for i in range(TN):
    ans1+=sum(A[i])
    for j in range(TN):
        if not visited[i][j] and A[i][j]:
            count=1
            visited[i][j]=True
            dfs([[i,j]])
            ans2=max(ans2, count)

print(ans1)
if ans2!=1: print(ans2)
else: print(ans1)