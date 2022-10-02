from collections import defaultdict, deque

def solution(dirs):
    ans, y, x = 0, 0, 0
    dic = defaultdict(list)
    dic['U'] = (-1, 0); dic['D'] = (1, 0); dic['R'] = (0, 1); dic['L'] = (0, -1)
    visit = deque()
    for i, d in enumerate(dirs):
        ny, nx = dic[d][0] + y, dic[d][1] + x
        if ny > 5 or nx > 5 or ny < -5 or nx < -5: continue
        tmp =  sorted([(ny, nx), (y, x)]) 
        if not tmp in visit: 
            ans += 1
            visit.append(tmp)
        y, x = ny, nx
    
    return ans