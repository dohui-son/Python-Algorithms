from collections import defaultdict, deque

def solution(s):
    st = deque()
    for ss in s:
        if ss == '(':st.append('(')
        else:
            if st : st.pop()
            else: return False

    if st: return False
    else: return True