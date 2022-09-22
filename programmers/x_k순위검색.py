from collections import defaultdict, deque
from itertools import combinations
from bisect import bisect_left

def solution(info, Q):
    ans = []
    n = len(info)
    dic = defaultdict(list)

    for i in range(n):
        tmp = info[i].split()
        strr = tmp[:-1]
        score = int(tmp[-1])
        for cnt in range(5):
            for c in combinations(strr, cnt): dic[ ''.join(c) ].append(score)
    for k in dic: dic[k].sort()

    for q in Q:
        tmp = q.split(' and ')
        st = ''
        for i in range(3):
            if tmp[i] == '-': continue
            st += tmp[i]

        s, score = tmp[-1].split(); score = int(score)
        if s!='-': st+=s 
        if dic[st]:
            idx = bisect_left(dic[st], score )
            ans.append(len(dic[st]) - idx)
        else: ans.append(0)

    return ans



    # 레퍼런스
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()


    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)

    return answer