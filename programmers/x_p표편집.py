from collections import defaultdict, deque
from bisect import bisect_left
# input : 5<= n <=1,000,000    0<=k<=n.   1<= cmd <= 200,000
#             표의 행            처음 선택된 행    cmd 원소 개수

def solution(n, k, cmd):
    ans = ['O']*n
    now = k
    llist = defaultdict(int)
    for i in range(n): 
        if i == n-1: llist[i] = [i-1, -1]
        else: llist[i] = [i-1, i+1]
    stk = deque()
    for c in cmd:
        l = c.split()
        if l[0] == 'U': 
            x = int(l[1])
            for xx in range(x): 
                if llist[now][0] == -1: break
                now = llist[now][0]

        elif l[0] == "D": 
            x = int(l[1])
            for xx in range(x):
                if llist[now][1] == -1: break
                now = llist[now][1]

        elif l[0] == "C":
            stk.append( ( llist[now][0], llist[now][1]  , now )) 
            ans[now] = 'X'
            if llist[now][1] == -1: 
                now = llist[now][0]
                llist[now][1] = -1
            else: 
                pre, nextt = llist[now]
                if pre>-1: llist[pre][1] = nextt
                llist[nextt][0] = pre
                now = nextt
        else: 
            if stk:
                pre, nextt, my_index = stk.pop()
                ans[my_index] = 'O'
                if pre == -1: llist[nextt][0] = my_index
                elif nextt == -1: llist[pre][1] = my_index 
                else: 
                    llist[nextt][0] = my_index
                    llist[pre][1] = my_index
    return ''.join(ans)