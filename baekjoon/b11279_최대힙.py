#최대힙 - 5분
from collections import defaultdict,deque
from itertools import combinations, permutations
from sys import stdin; reader = stdin.readline
import heapq as hq

q = []

n = int(reader().rstrip())
for _ in range(n): 
    x = int(reader().rstrip())
    if x:hq.heappush(q, -x )
    else:
        if q: print( -(hq.heappop(q)) )
        else: print(0)