from itertools import combinations, permutations

def solution(name):
    aord = ord('A')
    ans = 10000000000
    pre, total, n = 0, 0, len(name)
    arr = []
    for i in range(len(name)):
        if name[i] == 'A': continue
        total += min( (ord(name[i])-aord), 26 - (ord(name[i])-aord) )
        if i > 0: arr.append(i)
    for p in permutations(arr, len(arr)):
        pre, res = 0, total
        for num in p:
            l, r = min(pre, num), max(pre, num)
            res += min(r-l, n-r+l)
            pre = num
        if ans > res: ans = res
    return ans 