def solution(A):
    arr = []
    for i, v in enumerate(A):
        arr.append((i-v, -1))
        arr.append((i+v, 1))

    arr.sort()
    intersection = 0
    intervals = 0

    for i,v in enumerate(arr):
        if v[1] == 1 :
            intervals -= 1
        if v[1] == -1:
            intersection += intervals
            intervals += 1
    if intersection > 10000000:
        intersection = -1

    return intersection
# ref - https://sooho-kim.tistory.com/49