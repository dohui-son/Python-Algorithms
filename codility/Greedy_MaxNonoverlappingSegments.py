def solution(A, B):
    arr = [sorted([a,b], reverse=True) for a, b in zip(A, B) ]
    arr.sort()
    ans, pre = 0, -1 
    for a in arr:
        if pre < a[1]: 
            ans += 1
            pre = a[0]  
    return ans