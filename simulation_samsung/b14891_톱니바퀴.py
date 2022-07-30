from collections import deque # 톱니바퀴  1시간 15분
dq1 = deque(); dq2 = deque(); dq3 = deque(); dq4 = deque();
for i in range(4):
    l = input().rstrip()
    for ii in l:
        j = int(ii)
        if i == 0 : dq1.append( j )
        elif i == 1: dq2.append(j)
        elif i == 2: dq3.append(j)
        else: dq4.append(j)
k=int( input().rstrip())


def finddir(tirenum, st): #st 는 left 나 right
    if st == 'right':
        if tirenum == 1: return dq1[2]
        elif tirenum == 2: return dq2[2]
        elif tirenum == 3: return dq3[2]
        else : return dq4[2]
    else:
        if tirenum == 1: return dq1[6]
        elif tirenum == 2: return dq2[6]
        elif tirenum == 3: return dq3[6]
        else : return dq4[6]


def rotating(tire, clock):
    if tire == 1: dq1.rotate(clock)
    elif tire == 2: dq2.rotate(clock)
    elif tire == 3:dq3.rotate(clock)
    else: dq4.rotate(clock)




def play(tire,cdir):
    dq = deque( []); dq.append((tire,cdir))
    no = False; nowdir = cdir
    for i in range(1,5):#오른쪽 다 살펴봄
        if no: break
        if tire+i <= 4:
            if finddir(tire+i-1, 'right') != finddir(tire+i, 'left'):
                dq.append( (tire+i, -nowdir ) ); nowdir = -nowdir
            else: no = True; break
        else: break
    no = False; nowdir = cdir
    for i in range(1,5):#왼쪽 다 살펴봄
        if no : break
        if tire-i >= 1:
            if finddir(tire-i+1, 'left') != finddir(tire-i, 'right'):
                dq.append( (tire-i, -nowdir ) ); nowdir = -nowdir
            else: no = True; break
        else: break
    for d in dq:
        rotating(d[0],d[1])


for i in range(k):
    tire, cdir = map(int, input().split());
    play(tire,cdir)
print(dq1[0] +  dq2[0]*2 + dq3[0]*4 + dq4[0]*8)