import sys; reader = sys.stdin.readline
#비트마스킹 이용안하면 시간 초과가 난다.
def search(col, ld, rd, n):
    size = ((1 << n) - 1)
    count = 0

    if col == size:
        return 1

    slots = ~(col | ld | rd) & size
    while slots:
        bit = slots & -slots
        count += search(col | bit, (ld | bit) >> 1, (rd | bit) << 1, n)
        slots -= bit
    return count


def solution(n):
    return search(0, 0, 0, n)
n = int( reader().rstrip() )
print(solution(n))