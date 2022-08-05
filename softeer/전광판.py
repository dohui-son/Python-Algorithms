import sys 
sys.setrecursionlimit(5000)
from collections import deque, defaultdict
reader = sys.stdin.readline
num = defaultdict(int)
num[0] = (  (1<<0) | (1<<1) | (1<<2) | (1<<3) | (1<<4)  | (1<<5) ) 
num[1] = ( (1<<1) | (1<<2) )
num[2] = ( (1<<0) | (1<<1) | (1<<6) | (1<<3) | (1<<4) )
num[3] = ( (1<<0) | (1<<1) | (1<<6) | (1<<3) | (1<<2) )
num[4] = ( (1<<1) | (1<<2) | (1<<5) | (1<<6) )
num[5] = ( (1<<0) | (1<<2) | (1<<3) | (1<<5) | (1<<6) )
num[6] = ( (1<<0) | (1<<2) | (1<<3) | (1<<4) | (1<<5) | (1<<6) )
num[7] = ( (1<<1) | (1<<2) | (1<<5) | (1<<0) )
num[8] = (1<<7)-1 
num[9] = ( (1<<7)-1 ) ^ (1<<4)

n = int(reader().rstrip())
ans = [7*5]*n
for i in range(n):
    a, b = reader().split()
    arr = [0]*5; idx = 4 ; brr = [0]*5; ans = 0 ; bit = 0
    for i in range( len(a)-1,-1,-1 ): arr[idx] = int(i); idx -= 1
    idx = 4
    for i in range( len(b)-1,-1,-1 ):  arr[idx] = int(i); idx -= 1
    ansarr = [0]*5
    for i in range(4): 
        if brr[i]: # 1-9

        else: # 0
            if i == 0: # 전광판에 아무것도 안 띄워야하는 경우
                ansarr[i] = -1
                ans += bin(num[a[i]]).count('1')
            elif ansarr[i-1] == -1: # 전광판에 아무것도 안 띄워야하는 경우
                ansarr[i] = -1
                ans += bin(num[a[i]]).count('1')
            else:
                





        
    
