# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221137999832
# POW 에 대한 참고 *****

import sys #곱셈
# reader = sys.stdin.readline            ----->maximum recursion depth exceeded
# a,b,c = map(int,reader().split())
# def go(a,b):
#     if b == 1: return a%c
#     res = go(a,b/2)
#     res = (res*res)%c
#     if b%2: res = (res*a)%c
#     return res
# print(go(a,b))
reader = sys.stdin.readline
print(   pow( *map(int, reader().split()) ) ) # *은 여기서 언팩