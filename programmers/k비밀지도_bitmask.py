from collections import defaultdict,deque

def solution(n, arr1, arr2):
    ans = []
    for y in range(n):
        st = ""
        total = (1<<n)-1
        bit = arr1[y] | arr2[y]
        for i in range(n):
            if (1<<i)&bit: st+="#"
            else: st+=" "
        ans.append(st[::-1])

    return ans