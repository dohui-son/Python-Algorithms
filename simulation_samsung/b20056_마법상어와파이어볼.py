from collections import deque, defaultdict
from math import floor

nextdir = [[1,3,5,7],[0,2,4,6]]
dir = [ (-1, 0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1),(-1,-1) ]
n , m, K = map(int, input().split() )
fball = deque()
for _ in range(m):
    r,c,m,s,d = map(int, input().split()); r-=1; c-=1
    fball.append( [r,c,m,s,d] )

def move(y,x,ss,d):
    yy = ( y+dir[d][0]*ss ) % n
    xx = ( x+dir[d][1] * ss) % n
    if yy<0: yy+=n
    if xx < 0: xx += n
    return (yy,xx)

for kk in range( K ):
    dic = defaultdict(int)
    idx = 0; arr = [ [] for _ in range(n*n+1)]
    while fball:
        y, x, mass, sp, dd = fball.popleft()
        ny, nx = move(y,x,sp,dd)
        if (ny,nx) not in dic :
            dic[(ny,nx)] = idx
            arr[idx].append((ny,nx))
            arr[idx].append([mass, sp, dd])
            idx+=1
        else:
            tmp = dic[ (ny, nx) ]
            arr[ tmp ].append( [mass, sp,dd] )
    for keyy in dic:
        i = dic[keyy]
        if len( arr[i] ) == 2:
            y,x = arr[i][0]
            fball.append( [y,x,arr[i][1][0],arr[i][1][1],arr[i][1][2] ] )
        elif len( arr[i] ) > 2:
            total = len( arr[i] )-1
            y,x = arr[i][0]
            mm,ss = 0,0
            nn = len( arr[i] )
            hol = True; jjak = True # 있으면 false로 바뀜
            for f in range(1,nn):
                mass,sp,di = arr[i][f]
                mm += mass; ss += sp
                if di%2 == 0: jjak = False
                else: hol = False
            if floor(mm/5):
                nd = 0
                if hol == False and jjak == True: nd = 1
                elif hol == True and jjak == False: nd = 1
                for j in range(4) : fball.append( [y,x, floor(mm/5), ss//total,nextdir[nd][j]])
ans = 0
for f in fball:
    y, x, mass, sp, di = f
    ans += mass
print(ans)