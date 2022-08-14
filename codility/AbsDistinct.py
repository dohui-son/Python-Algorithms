def solution(A):
    se = set(A)
    visit, ans = 0, 0
    for i in se:
        s = abs(i)
        if not(visit & (1<<s) ):
            ans+=1 
            visit |= (1<<s)
    return ans