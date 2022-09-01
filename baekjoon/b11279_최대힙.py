#최대힙
from collections import defaultdict,deque
from itertools import combinations, permutations
import heapq as hq

q = []

n = int(input().rstrip())
for _ in range(n): 
    hq.heappush(q, -int(input().rstrip()) )
    print( -(hq.heappop(q)) )
