from collections import defaultdict, deque
def solution(numbers):
    st = map(str, numbers)
    q = sorted(st, key =  lambda x: x*3, reverse=True) 
    return str(int(''.join(q)))