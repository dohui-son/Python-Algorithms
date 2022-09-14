import math
def solution(arr):
    ans = 1
    for num in arr : ans = ans*num // math.gcd(ans, num)
    return ans