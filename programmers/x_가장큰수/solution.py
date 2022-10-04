def solution(numbers):
    st = [*map(str, numbers)]
    return str(int(''.join(sorted(st, key = lambda num: num * 3, reverse = True))))

    # https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html