def search(y, ld, rd, n):
    total = (1 << n) - 1
    if total == y: return 1
    cnt = 0
    bit = ~(y | ld | rd ) & total
    while bit:
        nextt = bit & -bit
        cnt += search(nextt | y, (ld | nextt) >> 1, (rd | nextt) << 1, n)
        bit -= nextt
    return cnt

def solution(n):
    return search(0, 0, 0, n)