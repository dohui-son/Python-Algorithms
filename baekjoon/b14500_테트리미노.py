from collections import defaultdict,deque
         # 파                 노                   주                     초                    핑
arr = [[ [(0,1),(0,2),(0,3)], [(0,1),(1,0),(1,1)], [(1,0),(2,0),(2,1)],  [(1,0),(1,1),(2,1)],  [ (0,1), (1,1),(0,2)] ], 
       [ [(1,0),(2,0),(3,0)] ,                     [(0,1), (0,2),(-1,2)],[(0,1),(-1,1),(-1,2)],[(0,1),(-1,1),(0,2)]],
       [                                           [(0,1),(0,2),(1,2)],  [(0,1),(1,1),(1,2)],  [(1,0),(1,1),(2,0)]], 
       [ [(1,0), (0,1), (0,2)],[(0,1),(1,1),(2,1)],  [(1,0),(1,1),(1,2)], [(0,1),(1,0),(2,0)]],
       [                                           [(1,0),(0,1),(-1,1)], [(1,1),(0,1),(-1,1)]]
]
ans = 0

n,m = map(int, input().split())
g = [[*map(int ,input().split())] for _ in range(n)]
for y in range(n):
    for x in range(m):
        if y == 1 and x==1:
           
            for i, tetri in enumerate( arr ):         
                for t in tetri:
                    g = [[1]*m for _ in range(n)]
                    summ, flag = g[y][x], True
                    g[y][x] = 0
                    for l in t:
                        ny,nx = y+l[0], x+ l[1]
                        if ny<0 or nx< 0 or ny>=n or nx>= m: flag=False; break
                        g[ny][nx] = 0
                        summ += g[ny][nx]
                    if flag: ans = max(ans, summ)
                    print()
                    for i in g: print(i)
print(ans)