def solution(X, Y, D):
    if X==Y : return 0
    y = Y-X
    if y%D: return y//D+1
    else: return y//D