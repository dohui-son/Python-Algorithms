from collections import defaultdict,deque
def solution(surv, choi):
    ans = ''
    score = [[0,0] for _ in range(4)]
    ch = [['R','T'],['C','F'],['J','M'],['A','N']]
    for i in range(4):
        if ord(ch[i][0])<ord(ch[i][1]): ch[i].append(ch[i][0])
        else:ch[i].append(ch[i][1])
        
    tonum = defaultdict(list)
    tonum['R'] = (0,0);tonum['T'] = (0,1);tonum['C'] = (1,0);tonum['F'] = (1,1);tonum['J'] = (2,0);tonum['M'] = (2,1);
    tonum['A'] = (3,0);tonum['N'] = (3,1);
    
    for i in range(len(choi)):
        if choi[i] == 4: continue
        
        if choi[i]<4: score[tonum[surv[i][0]][0]][tonum[surv[i][0]][1]] +=  (4-choi[i])
        else:score[tonum[surv[i][1]][0]][tonum[surv[i][1]][1]] +=  (choi[i]-4)
    for idx, s in enumerate(score):
        if s[0] > s[1]: ans += ch[idx][0]
        elif s[0] < s[1]: ans+= ch[idx][1]
        else: ans+= ch[idx][2]
        
    return ans