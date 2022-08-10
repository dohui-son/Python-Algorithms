def solution(A):
    alen = len(A)
    if alen == 0: return 1
    maxi = 0; visit = 1
    A.sort()
    for a in A:
        if a<=0: maxi = a
        else: 
            visit |= (1<<a)
            if a>maxi: maxi = a
    if maxi<=0: return 1
    else:
        full = (1<<maxi+1)-1
        if visit==full: return maxi+1
        bit = ~visit & full
        smallest = bit&-bit
        return bin(smallest)[::-1].index('1')