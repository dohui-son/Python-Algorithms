import sys #농구경기
reader = sys.stdin.readline
n = int(reader().rstrip())
arr = [0]*26
ans = ""

for i in range(n):
    str = reader().rstrip()
    arr[ord(str[0]) - ord('a')] += 1
    if arr[ord(str[0]) - ord('a')] >= 5 : ans += str[0]
if len( ans ) == 0 : print("PREDAJA")
else : 
    tosort = list( set(ans) )
    tosort.sort()
    print(*tosort, sep="")