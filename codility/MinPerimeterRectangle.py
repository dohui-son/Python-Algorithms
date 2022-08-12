def solution(N):
    ans = (N+1)*2
    for i in range(2,N):
        if (N/i)%1 == 0:
            if i**2 == N: ans = min(ans, (i+i)*2); break
            elif i < (N//i): ans = min( ans, (i+N//i)*2 )
            else: break
        elif i**2 > N: break
    return ans