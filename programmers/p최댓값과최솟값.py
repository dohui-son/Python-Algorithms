def solution(s):
    arr = [*map(int,s.split())]
    arr.sort()

    return str(arr[0])+' '+str(arr[-1])