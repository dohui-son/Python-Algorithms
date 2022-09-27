from collections import defaultdict,deque
global st, orda,ordz
st = deque( input() )
n = len(st)
stk = deque()
orda, ordz = ord('A'), ord('Z')
ans = ''

for s in st:
    if orda <= ord(s) <= ordz: ans += s
    else:
        if s == '(': stk.append(s)
        elif s == '*' or s == '/' :
            while stk and ( stk[-1] == '*' or stk[-1] == '/' ) : ans += stk.pop()
            stk.append( s )
        elif s == '+' or s == '-':
            while stk and stk[-1] != '(': ans += stk.pop()
            stk.append(s)
        elif s == ')':
            while stk and stk[-1] != '(': ans += stk.pop()
            stk.pop()
while stk : ans += stk.pop()

print(ans)  