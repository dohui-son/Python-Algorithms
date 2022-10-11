def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer



###############
from collections import defaultdict, deque
def solution(clothes):
    ans = 1
    dic = defaultdict(int)
    for c in clothes: dic[c[1]] += 1
    for k in dic: ans *= (dic[k]+1)
    return ans - 1