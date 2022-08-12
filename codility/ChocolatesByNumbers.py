# 시간 초과
def solution(N, M):
    visit = 1
    now, ans = 0, 1 
    for i in range(N):
        if now>=N:break
        if visit & (1<<(now+M)%N) : break
        else:  visit|=1<<((now+M)%N) ; ans+=1; now = (now+M)%N
    return ans




    # 시간초과 일부 개선됨 -  아래코드는 일부 수정 필요 - 수정전에 submit한 후 테스트 케이스 결과 먼저 보고 참고하기
def solution(N, M):
    now, ans = 0, 0
    for i in range(N):
        if now+(N//M)*M == N:ans+= N//M  ;break
        if now>0: ans+= N//M; now = (now + (N//M)*M)%N
        else: ans +=( N//M +1); now = (now + (N//M+1)*M)%N

    return ans