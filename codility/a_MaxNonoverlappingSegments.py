def solution(A, B):
    arr = []
    n = len(A)
    for i in range(n):
        a = A[i]; b = B[i]
        if a>b: a = B[i]; b = A[i] 
        arr.append((b, a))
    arr.sort()
    ans, pre = 1, arr[0][0]
    alen = len(arr)
    for i in range(1, alen):
        if pre < arr[i][0] and pre<arr[i][1]:
            ans+=1
            pre = arr[i][0]   
    return ans 