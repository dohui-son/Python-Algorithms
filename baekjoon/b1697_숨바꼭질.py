from collections import defaultdict,deque

n,k = map(int,input().split())
if n == k : print(0); exit()
k = k-n
n = 0
time = [0]*100001
q = deque([0])
while q:
    now = q.popleft()
    if time[now+1]
