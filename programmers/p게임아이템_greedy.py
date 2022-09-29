import heapq as hq

def solution(healths, items):
    ans, q, item = [], [], []
    healths.sort()
    
    for i, l in enumerate( items ):
        if healths[-1] - l[1] >= 100 : item.append((l[1], l[0], i+1))
    item.sort()
    
    idx, n = 0, len(item)
    for h in healths:
        while idx<n :
            need, att, num = item[idx]
            if 100 > h-need : break
            hq.heappush(q, (-att, num ) )
            idx += 1
        if q :
            minus, num = hq.heappop(q)
            ans.append(num)

    return sorted(ans)