from itertools import*
for c in combinations(map(int,open(0)),7):
 if sum(c)==100:print(*sorted(c),sep='\n');break