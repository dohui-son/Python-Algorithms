from collections import defaultdict, deque

arr = []
l = list( input() )
bomb = list(input())
n = len(bomb)

for s in l:
    arr.append(s)

    while len(arr)>=n :
        if arr[len(arr)-n:] == bomb: 
            for _ in range(n): arr.pop()
        else: break


if arr : print(*arr, sep="")
else : print('FRULA')