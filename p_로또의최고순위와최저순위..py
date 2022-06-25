def solution(lottos, win_nums):
    ans = [6,6]; cnt = 0
    zero = lottos.count(0)
    for i in lottos: 
        if i in win_nums: cnt += 1; win_nums.remove(i)
    if cnt+zero >= 2:
        ans[0] = 7 - cnt - zero
        if cnt : ans[1] = 7 - cnt
    return ans



##### 하기 모범답안
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]