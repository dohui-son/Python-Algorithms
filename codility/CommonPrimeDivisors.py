# https://mirae-kim.tistory.com/135 참고해서 풀어보기
def yaksoo(num):
    ret = (1<<num)
    for i in range(2, int(num**.5)+1):
        if num%i ==0:
            ret |= (1<<i)
            if num//i != i: ret |= ( 1 << (num//i) )
    return ret

def solution(A, B):
    n = len(A)
    ans = 0
    maxi = max( max(A), max(B)   )+1
    p = [0,0] + [1]*~-maxi
    prime = (1<<2)
    for i in range(int(maxi**.5)+1): 
        if p[i]: p[i*i::i] = [0]*(maxi//i-i+1)
    for i in range(3,maxi+1,2): 
        if p[i]: prime |= (1<<i)

    for i in range(n):
        y1 = yaksoo(A[i])
        y2 = yaksoo(B[i])
        if  prime & y1 == prime & y2: ans+=1
    return ans


