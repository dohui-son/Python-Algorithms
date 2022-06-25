import sys #팰린드롬 만들기
reader = sys.stdin.readline
s = reader().rstrip()
left, mid = "", ""
odd = 0
cnt = [0]*26

for c in s:
    cnt[ ord(c) - 65] += 1

for i in range(26):
    if cnt[i] % 2:
        odd += 1
        mid = chr( i +65 )   #아이디어
    left = left + chr( i + 65 ) * (cnt[i] // 2)   #아이디어

print( "I'm Sorry Hansoo" if odd > 1 else left + mid + left[::-1])