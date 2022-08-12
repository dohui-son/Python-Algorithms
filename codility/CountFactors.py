# 약수 개수 구하기
def solution(N):
    ans = 0
    for i in range(1,N+1):
        if (N/i)%1 == 0 : 
            if (N//i) == i: ans+=1; break
            elif i < (N//i): ans+=2
            elif i**2 > N: break
            else: break
        elif i**2>N:break
    return ans