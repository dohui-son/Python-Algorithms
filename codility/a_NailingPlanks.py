def check(a,b,c,num):
    pNails = [0]*(2*len(c)+1)
    for i in range(num+1): pNails[c[i]] +=1
    pnlen = len(pNails)
    for i in range(1, pnlen): pNails[i] += pNails[i-1]
    alen = len(a)
    for i in range(alen): 
        if pNails[b[i]] <= pNails[a[i]-1]:  return False
    return True

def solution(A, B, C):
    s, e, ans = 0, len(C)-1, -1
    while s<=e:
        mid = (s+e)//2
        if check(A,B,C,mid): 
            e = mid-1
            ans = mid+1
        else: s = mid+1
    return ans


# ref: https://velog.io/@j03y14/%EC%BD%94%EB%94%9C%EB%A6%AC%ED%8B%B0-NailingPlanks