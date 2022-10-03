def solution(brown, red):
    for a in range(1, red + 1):
        if red / a == red // a:
            if a * 2 + (red // a) * 2 + 4 == brown: 
                return [(red // a) + 2, a + 2] 