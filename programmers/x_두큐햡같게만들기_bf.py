from collections import defaultdict, deque

def solution(queue1, queue2):
    sum1,sum2,n = sum(queue1),sum(queue2), len(queue1)
    total = sum1+sum2
    q1 = deque( queue1 )
    q2 = deque( queue2 )
    if total%2 > 0 : return -1

    for i in range(n*3):
        if sum1 == sum2: return i
        if sum1 > sum2 and q1 :
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2 and q2:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
    
    return -1