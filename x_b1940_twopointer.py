#주몽  - 시간초과 투포인터  #투포인터(SORT 필수!!!!!시간 더 짧음)와 COMBINATION을 서로 착각할 수 있다
import sys
reader = sys.stdin.readline
n = int( reader().rstrip() ); m = int( reader().rstrip() )
arr = list( map(int, reader().split())); arr.sort() ######## SORT 필수
if m > 200000 : print(0); exit() 

lo , hi, cnt  = 0, n-1, 0
while lo < hi:
	if arr[lo] + arr[hi] == m : 
		cnt += 1 
		lo += 1
	elif arr[lo] + arr[hi] < m : lo += 1
	else : hi -= 1
	
print(cnt)



