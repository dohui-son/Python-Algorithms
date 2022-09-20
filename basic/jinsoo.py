def convert(n, k):  # 숫자 n을 str타입 k 진수로 바꾸기
    ret = ""
    while n > 0:
        ret += str(n % k)
        n //=  k
    return ret[::-1]