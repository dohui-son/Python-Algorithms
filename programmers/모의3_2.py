from collections import deque, defaultdict # 0
def solution(ingre):
    ans,n = 0,len(ingre)
    basic = deque([1,2,3,1])
    dq = []
    cnt = 0
    for i in range(n):
        dq.append(ingre[i]);cnt+=1
        if i>2 and dq:
            lenn = len(dq)
            while lenn>3:
                if dq[lenn-1] == basic[3] and dq[lenn-2] == basic[2] and dq[lenn-3] == basic[1] and dq[lenn-4] == basic[0]  : 
                    del dq[lenn-4:]; ans+=1
                else: break
                lenn = len(dq)


    return ans