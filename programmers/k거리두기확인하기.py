def check(g):
    visit = [[False]*5 for _ in range(5)]
    for y,yval in enumerate(g):
        for x, val in enumerate(yval):
            if y<4: 
                if g[y][x] == 'P' and g[y+1][x]==g[y][x]: return 0
            if x<4:
                if g[y][x] == 'P' and g[y][x+1]==g[y][x]: return 0
            if y<3: 
                if g[y][x] == 'P' and g[y+2][x] == 'P' and g[y+1][x] == 'O': return 0
            if x<3:
                if g[y][x] == 'P' and g[y][x+2] == 'P' and g[y][x+1] == 'O': return 0
            if y<4 and x<4:
                if g[y][x] == 'P' and g[y+1][x+1] == 'P' and ( g[y][x+1] == 'O' or g[y+1][x] == 'O'): return 0
            if y<4 and x>0:
                if g[y][x] == 'P' and g[y+1][x-1] == 'P' and ( g[y][x-1] == 'O' or g[y+1][x] == 'O'): return 0
    return 1

def solution(pl):
    ans = [0]*5
    for i in range(5): ans[i] = check(pl[i])

    return ans