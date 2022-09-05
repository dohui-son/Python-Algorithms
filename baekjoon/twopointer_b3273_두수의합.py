# 15 분
import sys; input = sys.stdin.readline;
sys.setrecursionlimit(5000)
from collections import defaultdict,deque,Counter
from math import factorial

n = int( input().rstrip() )
arr = [ *map(int , input().split()) ]
x = int(input().rstrip())
ans,s,e = 0,0,n-1
arr.sort()


# 버전 1 깜빡하지 않기
while s < e :
    if arr[s] + arr[e] == x : ans += 1

    if arr[s] + arr[e] < x : s += 1
    else : e -= 1
print(ans)




# 버전 2
# dic = defaultdict(int)
# for i in range(n):
#     nowcnt = dic[ arr[i] ]
#     ans += dic[x-arr[i]]
#     dic[arr[i]] += 1
# print(ans)