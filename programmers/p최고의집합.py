def solution(n, s):
    if n > s: return [-1]
    arr = [s//n]*n
    if s%n:
        summ = sum(arr)
        for i in range(n-1, -1, -1):
            summ += 1
            arr[i] += 1
            if summ == s: break
    return arr


    # multiple의 최대 결과를 위해서는 곱하는 수들의 차이가 가장 적어야한다
    def bestSet(n, s):
        answer = []
        a = int(s/n)
        if a == 0: return [-1]
        b = s%n
        for i in range(n-b):
            answer.append(a)
        for i in range(b):
            answer.append(a+1)

    return answer