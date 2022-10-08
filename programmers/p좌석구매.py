def solution(seat):
    seat = [(l[0], l[1]) for l in seat]
    return len(set(seat))