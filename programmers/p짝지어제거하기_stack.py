from collections import defaultdict,deque
def solution(s):
    st = deque()
    for ss in s:
        if st:
            if st[-1] == ss : st.pop()
            else: st.append(ss)
        else: st.append(ss)

    return 0 if st else 1