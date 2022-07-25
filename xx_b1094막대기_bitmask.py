import sys;reader = sys.stdin.readline  
n = int( reader().rstrip() ) ; ans = 1
while n!= 1:
    if (n & 1) : ans+=1 
    n //= 2
print(ans)


# 입력으로 들어온 숫자가 2^n 꼴의 숫자 몇개의 합으로 이루어지는지를 출력하면 되는 문제 --> 이를 이용