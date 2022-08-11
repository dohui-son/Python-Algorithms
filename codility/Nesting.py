from collections import deque
def solution(S):
    n = len(S)
    if n == 0: return 1
    st = deque()
    for s in S:
        if s == "(": st.append(s)
        elif s == ")": 
            if st: st.pop()
            else: return 0
    if st: return 0
    else: return 1