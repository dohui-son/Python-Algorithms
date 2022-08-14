def solution(A):
    fib = [0 for i in range(100001)]
    step = [-1 for i in range(len(A))]
    fib[1] = 1
    answer = -1
    lastfib = 0
    dest = len(A)
    
    for i in range(2, 100001) :
        fib[i] = fib[i-1] + fib[i-2]
        if(fib[i] > len(A)+1) :
            lastfib = i-1
            break
    for i in range(0, len(A)) :
        if A[i] == 1 :
            for j in fib[2:lastfib+1] :
                if i-j == -1 : step[i] = 1
                elif i-j >=0 and i-j < len(A) and A[i-j] == 1 and step[i-j] != -1:
                    if step[i] == -1 : step[i] = step[i-j] + 1
                    else : step[i] = min(step[i-j] + 1, step[i])
    for i in fib[2:lastfib+1] :
        if dest - i == -1 :
            answer = 1
            break
        elif dest-i >=0 and A[dest-i] == 1 and step[dest-i] != -1:
            if answer == -1 : answer = step[dest-i] + 1
            else : answer = min(answer, step[dest-i]+1)
            
    return answer