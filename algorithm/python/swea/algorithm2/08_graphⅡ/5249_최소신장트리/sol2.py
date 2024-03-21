import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def spanning_tree():
    min_heap = [(0,1)]
    result = 0
    while min_heap:
        weight, now = heappop(min_heap)
        if not visited[now]:
            visited[now] = 1
            result += weight
            for next_weight, next_node in graph[now]:
                if not visited[next_node]:
                    heappush(min_heap,(next_weight,next_node))
    return result

for tc in range(1,int(input())+1):
    V, E = map(int,input().split())
    graph = [[] for _ in range(E)]
    visited = [0] * (V+1)
    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append([w, e])
        graph[e].append([w, s])
    print(f'#{tc} {spanning_tree()}')