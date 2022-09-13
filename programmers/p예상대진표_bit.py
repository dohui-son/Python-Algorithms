def solution(n,a,b):
    for i in range(0,n**10):
        if a == b: return i
        else: 
            a = a//2+1 if a%2 else a//2
            b = b//2+1 if b%2 else b//2


# 다른 해결방법
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

# 숏코딩 비트마스킹
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()


# 1을 빼는 것은 선수의 위치를 0-index 형태로 바꾸기 위함인 것 같고요.


# a, b는 각각 선수의 위치이고 이를 2비트 수로 표현했을 때 
# a, b가 인접한 위치로 가려면, 두 비트가 같을 때는 0을 더하고 
# 두 비트가 다를 때는 1을 더하는 XOR 연산으로 생각할 수 있겠네요.
# 토너먼트 트리를 그렸을 때, 윗단을 최상위 비트, 
# 아래단을 최하위 비트로 생각하면 이해되실 것 같네요. 가령, 5(101)의 가장 앞의 비트값(최상위)가 트리의 꼭대기