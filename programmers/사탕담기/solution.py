from itertools import combinations, permutations


def solution(m, weights):
    ans, n = 0, len(weights)
    for i in range(1, n):
        for c in combinations(weights, i):
            if sum(c) == m: ans += 1
    return ans