from collections import defaultdict, deque

def solution(number, k):
    dq = []
    for num in number:
        while k>0 and dq and dq[-1] < num:
            dq.pop()
            k-= 1
        dq.append(num)

    return ''.join(dq[:len(dq)-k])