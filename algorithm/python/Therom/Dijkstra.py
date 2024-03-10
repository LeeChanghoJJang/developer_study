n, m =map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

# 1번부터 N+1번 노드까지 탐색하며, 방문하지 않음
# 최단 거리 테이블에서 거리가 가장 짧은 노드 선택
def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for end,cost in graph[start]:
        distance[end] = cost

    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for end,cost in graph[now]:
            distance[end] = min(distance[end],distance[now]+cost)

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
