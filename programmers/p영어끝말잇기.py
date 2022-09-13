from collections import defaultdict,deque
def solution(n, words):
    visit = defaultdict(int)
    visit[words[0]] = 1
    for i in range(1, len(words) ):
        if visit[words[i]] or words[i][0]!= words[i-1][-1] : return [i%n+1,i//n+1]
        visit[words[i]] = 1
    return [0,0] 
        
    # 숏코딩

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]