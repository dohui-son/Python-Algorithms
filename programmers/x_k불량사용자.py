from collections import defaultdict, deque
from itertools import permutations

def check(y,x):
    if len(y) != len(x): return False # 유의하기
    for a,b in zip(y,x):
        if b=='*': continue
        if a!=b: return False
    return True

def solution(user_id, banned_id):
    ans = []
    
    for i in permutations(user_id,len(banned_id)) :
        cnt = 0
        for a,b in zip(i,banned_id):
            if check(a, b) : cnt+=1
        if cnt == len(banned_id):
            if set(i) not in ans: ans.append(set(i)) #유의하기
    return len(ans)



    # 다른 풀이
    from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)