import sys
sys.stdin = open('input.txt')
# 우선순위 큐를 활용
from heapq import heappush,heappop

def prim(start):
    pq = []
    MST = [0] * V
    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # PRIM 가중치가 낮으면 먼저 나와야 한다.
    # --> 관리해야할 데이터 : 가중치, 노드 번호 2가지
    # --> 동시에 두 가지 데이터 다루기
    # 1. class로 만들기
    # 2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)
        print(now, MST)
        # 우선순위 큐의 특성 상 더 먼거리로 가는 방법이 큐에 저장되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면 continue
        # 방문 했다면 continue
        if MST[now]:
            continue
        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight
        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] ==0 or MST[to]:
                continue
            heappush(pq,(graph[now][to],to))

    print(f'최소비용 : {sum_weight}')

V, E = map(int,input().split())
# 인접 행렬로 저장
# - [실습] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int,input().split())
    # 가중치 저장
    graph[s][e] = w
    # 무방향 그래프
    graph[e][s] = w
prim(0)
# [가중치 그래프] 3-> 4로 가는데 31이라는 비용이 든다.
# graph[3][4] =31
print(graph)