# 0
def solution(dis, scope, time): #distance, scope, times
    ans,slen = 0, len(scope)
    arr = [False]*(dis+1)
    info = [-1]*(dis+1)
    for i in range(slen):
         scope[i].sort()
         l = scope[i]
         for j in range(l[0], l[1]+1):
             if j>dis:break
             info[j] = i
    for i in range(1,dis+1):
        if info[i] == -1: continue
        work,rest = time[info[i]]
        if 0<=(i-1)%(work+rest) and (i-1)%(work+rest)<work:return i

    # for i in range(slen):
    #     scope[i].sort()
    #     s,e = scope[i]
    #     work,rest = time[i]
    #     for j in range(s,e+1):
    #         if 0 <= j%(work+rest+1) and j%(work+rest+1)<work : 
    #             if s+j%(work+rest+1)<dis+1: arr[j] = True
    #             break  
    #         if j>dis: break

    if True in arr: 
        tmp = arr.index(True)
        if tmp<=dis: return tmp
    return dis