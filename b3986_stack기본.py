import sys #좋은 단어   #스택-----파이썬은 DEQUE 이용할것 st = collections.deque([])
import collections
reader = sys.stdin.readline
n = int(reader().rstrip())
ans = 0
s = list(reader().rstrip() for _ in range(n) )
for i in range(n):
    cnt = 0
    st = collections.deque([])
    for c in s[i]:
        if not st : st.append(c)    #스택 PUSH arr.append(값)   
        elif st[-1] == c : st.pop()       #리스트 마지막 값 조회 arr[-1]   
        else : st.append(c)               #스택 POP arr.pop()
    if len(st) == 0 : ans += 1
print(ans)