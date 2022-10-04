import heapq as hq

def solution(operations):
    q = []
    for st in operations:
        a, num = st.split()
        num = int(num)
        if a == 'I': hq.heappush(q, num)
        elif num == 1 and q: q.remove(max(q))
        elif num == -1 and q: hq.heappop(q)

    return [max(q), q[0]] if q else [0, 0]

# 최소힙
# 루트 노드는 최솟값임이 확실히 보장되나 모든 노드의 데이터는 자식 노드보다 작기만 하면 된다.

# 즉, 완전 이진 트리이면서 위 조건을 만족해야하기에 아래와 같은 트리 구조를 갖는다.

# 마지막 인덱스는 최댓값이라는 보장이 없다. --> 다음과 같은 경우가 있을수 있음
    #          1
	#     2        5
    # 4       3