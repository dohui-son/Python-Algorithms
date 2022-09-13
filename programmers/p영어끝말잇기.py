from collections import defaultdict,deque
def solution(n, words):
    visit = defaultdict(int)
    visit[words[0]] = 1
    for i in range(1, len(words) ):
        if visit[words[i]] or words[i][0]!= words[i-1][-1] : return [i%n+1,i//n+1]
        visit[words[i]] = 1
    return [0,0] 
        
    