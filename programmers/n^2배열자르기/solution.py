from collections import defaultdict, deque
def solution(n, left, right):
    small = left//n 
    arr = []
    flag = False
    for y in range(small,n+1):
        for x in range(n):
            if len(arr)+n*small-1 >= right: flag = True; break
            if x+1 > y+1: arr.append(arr[-1]+1)
            else: arr.append( y+1 )
        if flag: break
    return arr[left-n*small:]



# 숏코딩
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer