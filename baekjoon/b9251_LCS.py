from collections import defaultdict, deque

w1 = input().rstrip()
w2 = input().rstrip()
n,m = len(w1), len(w2)
memo = [0]*n
pre = w1[0]
if pre in w2 : memo[0] = 1
for i in range(1,n):
    if pre+w1[i] in w2:
        pre += w1[i]
        memo[i] = memo[i-1]+1
    else: 
        pre = w1[i]
        if pre in w2: memo[i] = 1
print(max(memo))


