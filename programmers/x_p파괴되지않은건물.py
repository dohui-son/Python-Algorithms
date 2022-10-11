def solution(board, skill): #[type, r1, c1, r2, c2, degree]
    ans = 0
    psum = [[0]*(len(board[0])+1)  for _ in range(len(board)+1)]

    for typ, r1, c1, r2, c2, degree in skill:
        psum[r1][c1] += (degree if typ == 2 else -degree)

        psum[r1][c2+1] -= (degree if typ == 2 else -degree)
        psum[r2+1][c1] -= (degree if typ == 2 else -degree)

        psum[r2+1][c2+1] += (degree if typ == 2 else -degree)

    for y in range(len(psum)-1):
        for x in range(len(psum[0])-1): psum[y][x+1] += psum[y][x] 
    for y in range(len(psum)-1):
        for x in range(len(psum[0])-1): psum[y+1][x] += psum[y][x]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] + psum[y][x] > 0: ans += 1
    return ans