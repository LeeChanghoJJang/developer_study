import sys
sys.stdin = open('input.txt')
from heapq import *

def dijkstra(start):
    heap = []
    heappush(heap,(0,start))
    dp[start] = 0
    while heap:
        now_wei, now = heappop(heap)
        if dp[now] <= now_wei:
            for cost, next_node in graph[now]:
                next_wei = now_wei + cost
                if dp[next_node] > next_wei:
                    dp[next_node] = next_wei
                    heappush(heap,(next_wei,next_node))

for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    dp = [int(1e9) for _ in range(V+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        graph[s].append([w,e])
    dijkstra(0)
    print(f'#{tc} {dp[-1]}')