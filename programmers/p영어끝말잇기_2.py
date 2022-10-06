import math
def solution(n, words):
    se = set()
    for i in range(len(words)):
        if i>0 and (words[i] in se or words[i-1][-1] != words[i][0]): return [i % n + 1, math.ceil((i+1) / n)]
        se.add(words[i])
    return [0, 0]