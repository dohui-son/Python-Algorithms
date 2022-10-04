def solution(s):
    ans, n = 1, len(s)
    if s == s[::-1]: return n
    for start in range(n):
        for e in range(start + 1, n):
            if e - start < ans: continue
            word = s[start:e + 1]
            if word == word[::-1]: ans = max(ans, len(word))
    return ans