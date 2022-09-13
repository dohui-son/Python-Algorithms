def solution(s):
    ret,zero = 0,0
    while s!='1':
        ret+=1
        total = len(s)
        lenn = s.count('1')
        zero += total-lenn
        s = bin( lenn )[2:]
        if s == '1': break
        
    return [ret, zero]