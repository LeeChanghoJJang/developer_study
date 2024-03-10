import sys
sys.stdin = open('input.txt')

N,M,V = map(int,input().split())

# 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a]=1

# dfs 함수만들기
def dfs(V):
    visited[V]=1
    print(V, end=' ')
    for i in range(N):
        if graph[V][i] and visited[i] == 0:
            dfs(V)

def bfs(V):
    queue = [V]
    visited[V] = 1
    while queue:
        now = queue.pop()
        for i in range(N):
            if graph[V][i] and visited[i] ==0:
                queue.append(i)
                visited[i]=1

