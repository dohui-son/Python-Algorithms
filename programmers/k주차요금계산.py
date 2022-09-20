from collections import defaultdict, deque
import math

def solution(f, records): # 기본 시간(분)  기본 요금(원)  단위 시간(분)  단위 요금(원)
    dic = defaultdict(list) # 입차, 출차
    time = defaultdict(int)
    endd = 23*60+59
    ans = []
    for r in records :
        t,num,inout = r.split()
        hr = int( t[0]+t[1] )
        m = int(t[3]+t[4])
        if dic[num]:
            if inout[0] == 'I': dic[num][0] = m+60*hr
            else: dic[num][1] = m+60*hr   
            time[num] += dic[num][1] - dic[num][0]
            del dic[num]
        else:
            if inout[0] == 'I': dic[num] = [m+60*hr, 0]
            else: dic[num] = [0,m+60*hr]
    if dic:
        for num in dic:
            s,e = dic[num]
            if e == 0: e = endd
            time[num] += (e-s)
    tt = sorted(time.items())
    for l in tt:
        num,t = l
        if t<= f[0] : ans.append(f[1])
        else:ans.append(f[1] + math.ceil( (t-f[0])/f[2] )*f[3] )

    return ans