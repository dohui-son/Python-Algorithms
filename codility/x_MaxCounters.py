# Detected time complexity: O(N + M)
def solution(N, A):
    maxi, nowmax = 0,0
    ans = [0]*N
    for a in A:
        if a <= N :
            if ans[a-1] < maxi: ans[a-1] = maxi
            ans[a-1]+=1
            if nowmax < ans[a-1]: nowmax = ans[a-1]
        else: maxi = nowmax
    for i in range(N):
        if ans[i] < maxi : ans[i] = maxi
    return ans    