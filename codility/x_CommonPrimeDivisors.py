from math import gcd
def solution(A, B):
    n, ans = len(A), 0
    for i in range(n):
        if A[i] == B[i]: ans+=1
        else:
            gcdd = gcd(A[i], B[i])
            a_gcd, b_gcd = 0,0
            while a_gcd != 1: a_gcd =  gcd(A[i], gcdd); A[i] //= a_gcd
            while b_gcd != 1: b_gcd =  gcd(B[i], gcdd); B[i] //= b_gcd
            ans = ans+1 if (A[i]==1 and B[i] ==1) else ans
    return ans

# 같은 소인수를 가진 A, B 쌍의 갯수를 찾는 문제이다.

# 각 수와 최대 공약수의 최대 공약수를 찾아 나누고, 
# 두 수가 모두 1이 되면 같은 소인수를 가진 것이다.

# 즉, (두 수의 인수) = (최대 공약수의 인수)인 경우를 찾는 것이다.