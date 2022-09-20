from collections import defaultdict,deque
def convert(n,k):
    ret = ''
    while n:
        ret += str(n%k)
        n//=k
    return ret[::-1]

def isPrime(num):
    if num==2 or num==3: return True
    if num%2 == 0 or num%3==0 or num<2 : return False
    for i in range(3, int(num**.5)+1, 2):
        if num%i == 0: return False
    return True

def solution(n, k):
    ans = 0
    st = convert(n,k).split('0')
    for s in st:
        if s == "": continue
        if isPrime(int(s)): ans += 1
    
    return ans