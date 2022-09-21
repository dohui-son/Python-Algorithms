import sys; sys.setrecursionlimit(10000)
from collections import defaultdict

def findEmpty(num, parent):
    if parent[num] == 0: # 빈방이므로 다음에 이 방 요청시에 그 다음 빈방 번호 업데이트해둠
        parent[num] = num+1
        return num
    nextt = findEmpty(parent[num], parent) # 해당방이 이미 찼으므로 부모노드 탐색
    parent[num] = nextt+1 # 부모노드 갱신
    return nextt

def solution(k, rn):
    n = len(rn)
    ans = [0] * n
    parent = defaultdict(int)
    
    for num in rn:
        ret = findEmpty(num, parent)

    return list(parent.keys())