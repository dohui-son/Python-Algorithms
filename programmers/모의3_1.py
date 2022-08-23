def solution(a, b, n):
    ans = 0
    if n<a: return ans
    bottle,ans = n,0
    while bottle>=a:
        res = bottle//a*b
        if bottle//a : bottle-= (bottle//a)*a
        bottle+=res ; ans+=res
        
    return ans