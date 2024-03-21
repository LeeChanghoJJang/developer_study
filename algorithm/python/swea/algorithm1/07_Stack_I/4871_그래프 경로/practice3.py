import sys
sys.stdin = open('input2.txt')
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS(start):
    stack = [start] # 다음 조사 대상
    while stack: # 조사 대상이 없어질 때까지
        now = stack.pop() # LIFO
        if visited[now]==0:
            visited[now] = 1
        print(now,end=' ')
        # 다음번 조사 대상이 누구냐 --> 인접리스트 adj[now] 대상 모두 조사
        for next in adj[now]:
            if visited[next]==0:
                stack.append(next)


V,E = map(int,input().split())
arr = list(map(int,input().split()))
adj = [[] for _ in range(V+1)] # 0번 노드 없음
visited = [0] * (V+1)
for i in range(V+1):
    print(adj[i])

for idx in range(0,E*2,2): # 간선의 개수는 개당 2개의 노드번호 가짐
    print(idx, idx+1)
    print(arr[idx],arr[idx+1])
    from_node = arr[idx]
    to_node = arr[idx+1]
    # 무 방향 그래프니까 반대로도 넣기
    adj[from_node].append(to_node)
    adj[to_node].append(from_node)


# for idx in range(E):
#     adj[arr[idx*2]].append(arr[idx*2+1])
#     adj[arr[idx * 2+1]].append(arr[idx*2])

DFS(1)
print(adj)

