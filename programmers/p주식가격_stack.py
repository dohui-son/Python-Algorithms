from collections import defaultdict, deque
def solution(prices):
    ans = [0]*len(prices)
    stk = deque()
    for i in range(len(prices)):
        while stk and prices[stk[-1]] > prices[i]:
            idx = stk.pop()
            ans[idx] = i - idx
        stk.append(i)
    while stk:
        idx = stk.pop()
        ans[idx] = len(prices) - idx - 1
    return ans