### BFS
def BFS(G,v):
    visited = [0]*(n+1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visit(t)
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V,E = map(int,input().split())
arr = list(map(int,input().split()))
# 인접 리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 무향 그래프