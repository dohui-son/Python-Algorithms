def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i>0 and arr[i-1] == arr[i]: continue
        ans.append(arr[i])
    return ans