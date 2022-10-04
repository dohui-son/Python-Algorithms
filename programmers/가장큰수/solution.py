def solution(numbers):
    st = [*map(str, numbers)]
    return str(int(''.join(sorted(st, key = lambda num: num * 3, reverse = True))))