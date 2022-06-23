from itertools import* #일곱 난쟁이

for c in combinations(map(int,open(0)),7):
 if sum(c)==100:print(*sorted(c),sep='\n');break

 #combination / bruteforce