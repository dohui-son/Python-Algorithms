import sys #트럭주차
reader = sys.stdin.readline

abc = list( map(int, reader().split()) )
arr = [(0,0)] * 3
for i in range(3):
    s,e = map(int, reader().split() )
    arr[i] = (s,e)
arr.sort()
ans = 0
for i in range(101 - arr[0][0]):
    cnt = 0
    i += arr[0][0]
    if(i >= arr[0][0]) and (i < arr[0][1]) : cnt += 1
    if(i >= arr[1][0]) and (i < arr[1][1]) : cnt += 1
    if(i >= arr[2][0]) and (i < arr[2][1]) : cnt += 1
    ans += (abc[cnt-1] * cnt )
print(ans)
