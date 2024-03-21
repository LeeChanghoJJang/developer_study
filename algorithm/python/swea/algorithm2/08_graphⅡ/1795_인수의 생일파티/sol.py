import sys
sys.stdin = open('input.txt')
from heapq import *

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    dp = [int(1e9)] * (V + 1)
    dp[start] = 0
    while heap:
        now_wei, now = heappop(heap)
        if dp[now] < now_wei:
            continue
        for cost, next_node in graph[now]:
            next_wei = now_wei + cost
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heappush(heap, (next_wei, next_node))
    return dp

for tc in range(1, int(input()) + 1):
    V, E, X = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    max_time = 0
    dp_to_x = dijkstra(X)
    for i in range(1, V + 1):
        if i == X:
            continue
        dp_from_x = dijkstra(i)
        max_time = max(max_time, dp_to_x[i] + dp_from_x[X])

    print(f'#{tc} {max_time}')
