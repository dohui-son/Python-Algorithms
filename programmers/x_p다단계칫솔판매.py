from collections import defaultdict, deque
import math

def findd(now, money, tonum, parent,ans):
    if parent[now] == now or money//10 == 0: 
        ans[now] += money
        return
    give = money//10
    ans[now] += (money - give)
    findd(parent[now], give, tonum, parent, ans)

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    ans = [0]*(n+1)
    parent = [i for i in range(n+1)]
    tonum = defaultdict(int); tonum['-'] = 0
    for i, e in enumerate(enroll): tonum[e] = (i+1)
    for i in range(n): parent[i+1] = tonum[referral[i]]

    for i in range(len(seller)): findd(tonum[seller[i]], amount[i]*100, tonum, parent, ans)
    return ans[1:]