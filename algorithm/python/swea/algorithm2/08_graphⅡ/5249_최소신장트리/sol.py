import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def spanning_tree(start):
    min_heap = []
    result = []
    heappush(min_heap,(0,start))
    while min_heap:
        wei, now = heappop(min_heap)
        if not visited[now]:
            visited[now] = 1
            result.append(wei)
            for next_wei, next_node in graph[now]:
                if not visited[next_node]:
                    heappush(min_heap,(next_wei,next_node))
    return sum(result)

for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    graph = [[] for _ in range(E)]
    visited = [0] * (V+1)
    for i in range(E):
        s,e,w = map(int,input().split())
        graph[s].append([w,e])
        graph[e].append([w,s])

    print(f'#{tc} {spanning_tree(1)}')