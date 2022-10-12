import sys; sys.setrecursionlimit(10**6)
from collections import defaultdict, deque

def pre_order(yyy, xxx, ans):
    now = yyy[0]
    x_idx = xxx.index(now)
    ly, ry = deque(),deque()
    for x, y, num in yyy:
        if x < now[0]: ly.append([x,y,num])
        elif x> now[0]: ry.append([x,y,num]) 
    ans.append(now[2])
    if ly: pre_order(ly, xxx[:x_idx], ans)
    if ry: pre_order(ry, xxx[x_idx+1:], ans)

def post_order(yyy, xxx, ans):
    now = yyy[0]
    x_idx = xxx.index(now)
    ly, ry = deque(), deque()
    for x, y, num in yyy:
        if x < now[0]: ly.append([x, y, num])
        elif x > now[0]: ry.append([x, y, num])
    if ly: post_order(ly, xxx[:x_idx], ans)
    if ry: post_order(ry, xxx[x_idx+1:], ans)
    ans.append(now[2])

def solution(nodeinfo):
    n = len(nodeinfo)
    pre_ans, post_ans = [], []

    for i in range(n): nodeinfo[i].append(i+1)
    y_info = sorted(nodeinfo, key = lambda x: -x[1] )
    x_info = sorted(nodeinfo)

    pre_order(y_info, x_info, pre_ans)
    post_order(y_info, x_info, post_ans)
    return [pre_ans, post_ans]