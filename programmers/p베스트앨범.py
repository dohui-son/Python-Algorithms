from collections import Counter, defaultdict
def solution(genres, plays):
    ans, q = [], []
    gen = defaultdict(int)
    for i in range(len(plays)): gen[genres[i]] += plays[i]
    arr = [(gen[genres[i]], plays[i], -i, genres[i]) for i in range(len(plays))]
    arr = sorted(arr, key = lambda x: (-x[0], -x[1], -x[2]) )
    pre, cnt = "", 0
    for a in arr:
        if pre == a[3] and cnt == 2: continue
        if pre != a[3]: cnt = 0
        pre = a[3]
        cnt += 1
        ans.append(-a[2])
    return ans