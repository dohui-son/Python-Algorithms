from collections import defaultdict,deque

global t,r,c,m,shark,g
dir = [(-1,0),(1,0),(0,1),(0,-1)]
#        0      1    2      3
shark = defaultdict(list)
ans = 0

r,c,m = map(int,input().split())
g = [[0]*c for _ in range(r)]
live = deque()
for _ in range(m):
    y,x,f,d,w = map(int,input().split())
    y,x,d = y-1,x-1,d-1
    shark[w] = [y,x,d,f]
    g[y][x] = w
    live.append(w)

def sharkmove():
  global t,r,c,m,shark,g
  
  kk = live.copy()
  g = [[0]*c for _ in range(r)]
  
  for w in kk:
    yy,xx,d,f = shark[w]
    
    tt,y,x = f,yy,xx
    
    if d<2: tt%= (r-1)*2
    else: tt%=(c-1)*2
    
    while tt:
      ny,nx = y+dir[d][0]*tt, x+dir[d][1]*tt
      if ny<0 or nx<0 :
        if ny<0 : tt -= y; y = 0; d = 1
        else: tt -= x; x = 0; d = 2
      elif ny>=r or nx>=c:
        if ny>=r : tt -= (r-1-y); y = r-1; d = 0
        else: tt -= (c-1-x); x = c-1; d = 3
      else: y,x = ny,nx; tt = 0
    
    if g[y][x]>0 and g[y][x]>w: 
      live.remove(w)
      del shark[w]; continue
    elif g[y][x]>0 and g[y][x]<w: 
      live.remove(g[y][x])
      del shark[g[y][x]]
    g[y][x] = w
    shark[w] = [y,x,d,f]



for xx in range(c):
    for yy in range(r):
        if g[yy][xx]>0:
            ans +=g[yy][xx]
            del shark[g[yy][xx]]
            live.remove( g[yy][xx] ) 
            g[yy][xx] = 0
            break
    sharkmove()
  
print(ans)