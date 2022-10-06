from collections import defaultdict, deque
import heapq as hq

def solution(scoville, K):
    ans = 0
    hq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)

        hq.heappush(scoville, a + b*2)
        ans += 1
    
    return -1 if scoville[0] < K else ans