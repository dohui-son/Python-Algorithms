#Manhattan skyline 문제 - O(N)
from collections import deque
def solution(H):
    n = len(H)
    if n <= 1: return n
    ret = 1
    st = deque([H.pop(0)])
    for h in H:
        if h > st[-1]:
            st.append(h)
            ret+=1
        elif h < st[-1]:
            while st and (h<st[-1]): st.pop()
            if not st or h != st[-1]:
                ret+=1
                st.append(h)
    return ret