from collections import defaultdict, deque
INF = 1000001
n = int(input().rstrip())
memo = [INF]*(n+1)
memo[1] = 0
if n <= 1 : print(0); exit(0)
if n == 2 : print(1); exit(0)
memo[2] = 1
memo[3] = 1
for i in range(4,n+1):
    if i/2%1 == 0: memo[i] = memo[i//2]+1
    else : memo[i] = memo[(i-1)//2]+2
    if i/3%1 == 0: memo[i] = min( memo[i], memo[i//3]+1 )
    elif (i-1)/3%1 == 0: memo[i] = min( memo[i], memo[(i-1)//3]+2 )
    memo[i] = min(memo[i-1]+1, memo[i])
    
print(memo[n])
    
