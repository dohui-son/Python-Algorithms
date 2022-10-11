from collections import defaultdict, deque
import math
def solution(progresses, speeds):
    answer = []
    pre = -1
    for p,s in zip(progresses, speeds):
        now = math.ceil((100-p)/s)
        if now > pre: 
            pre = now
            answer.append(1)
        else: answer[-1] += 1
    return answer