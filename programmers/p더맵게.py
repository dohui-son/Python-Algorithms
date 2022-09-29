from collections import defaultdict, deque
import heapq as hq

def solution(scoville, K):
    ans = 0
    hq.heapify(scoville)
    while scoville[0] < K:
        try: 
            hq.heappush(scoville, hq.heappop(scoville) + hq.heappop(scoville)*2 )
            ans += 1
        except: return -1
    
    return ans