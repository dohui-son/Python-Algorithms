from collections import defaultdict, deque
from bisect import bisect_left

# 미래 T 분 동안 먹을 N 종류의 음식에 대해 각각의 음식을 먹을 시각을 분 단위로 표시한 길이 N의 목록
# D 분 동안 다이어트 효과가 유지되는데, 심모 양은 총 K 잔의 김네마 실베스터 차를
t,n,d,k = map(int,input().split())
arr = list(map(int,input().split()))
 
arr.sort()
arr = [0] + arr
dcnt = [0]*(n+1) # i번째 음식먹을 때 차를 마신다면
for i in range(1, n+1): dcnt[i] = bisect_left(arr, arr[i]+d ) - i 

dp = [ [0]*(k+1) for _ in range(n+1)]
for kk in range(1, k+1):
    for nn in range(1, n+1):
        drink = dcnt[nn]
        dp[nn][kk] = max(dp[nn-1][kk], drink + dp[nn-drink][kk-1])
print(dp[n][k])