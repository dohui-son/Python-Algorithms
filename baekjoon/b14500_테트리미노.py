from collections import defaultdict,deque
arr = [[ [(0,1),(0,2),(0,3)], [(0,1),(1,0),(1,1)], [(1,0),(2,0),(2,1)],  [(1,0),(1,1),(2,1)],  [ (0,1), (1,1),(0,2)] ], 
       [ [(1,0),(2,0),(3,0)] ,                     [(0,1), (0,2),(-1,2)],[(0,1),(-1,1),(-1,2)],[(0,1),(-1,1),(0,2)]],
       [                                           [(0,1),(0,2),(1,2)],  [(0,1),(1,1),(1,2)],  [(1,0),(1,1),(2,0)]], 
       [ [(1,0), (0,1), (0,2)],[(0,1),(1,1),(2,1)],  [(1,0),(1,1),(1,2)], [(0,1),(1,0),(2,0)]],
       [   [(0,1),(-1,1),(-2,1)],                                        [(1,0),(0,1),(-1,1)], [(1,1),(0,1),(-1,1)]]
]
ans = 0
n,m = map(int, input().split())
g = [[*map(int ,input().split())] for _ in range(n)]
for y in range(n):
    for x in range(m):
        for i, tetri in enumerate( arr ):         
            for t in tetri:
                summ, flag = g[y][x], True
                for l in t:
                    ny,nx = y+l[0], x+ l[1]
                    if ny<0 or nx< 0 or ny>=n or nx>= m: flag=False; break
                    summ += g[ny][nx]
                if flag: ans = max(ans, summ)    
print(ans)