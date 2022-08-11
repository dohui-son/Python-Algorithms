from collections import deque
def solution(A, B):
    bmin = min(B); bmax = max(B)
    if bmin == bmax: return len(B)
    up_down,sizee = -1, 0; n = len(A)
    ans = n
    st = deque()
    for i in range (n):
        if B[i] == 0 : 
            while st: # while 문을 돌려서 만약 물고기가 계속 잡아먹을 수 있으면 잡아먹게하는 것을 깜박함
                if A[i] > st[-1]: st.pop(); ans-=1
                else: ans -= 1; break
        elif B[i]: st.append(A[i])
    return ans