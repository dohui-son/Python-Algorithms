import sys #ROT13
reader = sys.stdin.readline
str = reader().rstrip()
ans = ""
a = 0

for c in str : 
    if ( c == " ") or ( ord(c) < ord('A') ): 
        ans += c
        continue
    if ord(c) > ord('Z') : a = ord('a')
    else : a = ord('A')
    ans += chr( (ord(c)+13 - a) % 26 + a)
print(ans)

# if(s[i] >= 65 && s[i] < 97){ 대문자인 경우
# }else if(s[i] >= 97 && s[i] <= 122){ 소문자인 경우