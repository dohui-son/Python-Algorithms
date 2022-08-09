def solution(board, moves):
    ans = 0; n = len(board)
    st = []
    idx = [0]* n
    for m in moves:
        m -= 1
        if idx[m] >= n:continue
        num = idx[m]
        while num<n:
            if board[num][m]>0:break
            num+=1
        idx[m] = num
        if num >= n: continue
        idx[m] += 1
        if st:
            if st[-1] == board[idx[m]-1][m] : st.pop();ans+=2; continue
        if board[idx[m]-1][m]>0: st.append(board[idx[m]-1][m] )
    return ans