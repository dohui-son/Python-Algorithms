from collections import defaultdict, deque
def solution(record):
    ans = []
    toname = defaultdict(str)
    for r in record:
        l = r.split()
        if l[0][0] == 'E' or l[0][0] == 'C': toname[l[1]] = l[2]

    for r in record:
        l = r.split()
        if l[0][0] == 'E': ans.append(toname[l[1]]+"님이 들어왔습니다.")
        elif l[0][0] == 'L':ans.append(toname[l[1]]+"님이 나갔습니다.")

    return ans