def solution(X, A):   
    full = (1<<X+1)-1
    visit = 1
    for idx,i in enumerate(A):
        if i>X: continue
        visit |= (1<<i)
        if visit == full : return idx
    return -1