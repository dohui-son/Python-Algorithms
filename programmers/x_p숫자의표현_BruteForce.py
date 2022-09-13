def solution(n):
    ans = 0
    if n<=2: return 1
    for s in range(1,n+1):
        summ = 0
        for num in range(s,n+1):
            summ+=num
            if summ > n : break
            elif summ == n : ans+=1; break
    return ans