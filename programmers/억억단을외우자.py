arr = [[1,i] for i in range(5000001)]

def createDivisor(s, e):
    
    for i in range(s,e+1):
        for j in range(1, i//2+1):
            if i % j == 0: arr[i][0] += 1
            


def solution(e, starts):
    k = [2,1]
    sorted_s = sorted(k)
    print(k)

    answer = []
    mini = min(starts)
    createDivisor(mini, e)
    print(sorted_s)
    print(starts)
    
    
    return answer