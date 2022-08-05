import sys
from collections import defaultdict, deque
reader = sys.stdin.readline
n,k = map(int,reader().split())
srr = list( map(int,reader().split()))
psum = [0]*(n+1)
for i in range(1,n+1):psum[i] = psum[i-1]+srr[i-1]

for i in range(k):
    a,b = map(int,reader().split())
    if a>b: tmp = b; b = a; a= tmp
    print( format((psum[b]-psum[a-1])/(b-a+1),'.2f') )