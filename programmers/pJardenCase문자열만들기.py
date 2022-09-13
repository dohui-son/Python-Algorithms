def solution(s):
    s = s.lower()
    ret = ''
    for i in range(len(s)):
        if s[i-1] == ' ' or i==0 : ret+= s[i].upper()
        else: ret += s[i]
    return ret