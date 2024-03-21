import sys
sys.stdin = open('input2.txt')

def DFS(start):
    visited[start] =1 # 다음 조사 대상
    print(start,end=' ')
    for next in range(1,V+1):
        if visited[next]==0 and adj[start][next] == 1:
            DFS(next)

V,E = map(int,input().split())
arr = list(map(int,input().split()))
visited = [0] * (V+1)

# 인접 행렬
adj = [[0] * (V+1) for _ in range(V+1)]
print(arr)

for idx in range(E):
    adj[arr[idx*2]][arr[idx*2+1]] = 1
    adj[arr[idx * 2+1]][arr[idx * 2]] = 1

for i in range(V+1):
    print(adj[i])
DFS(1)










'''
N=1 ---> 순열 [1] 순서쌍도 (1,1)
N=2   1<=l,r <=N 
---> 순열 [1,2], [2,1] (1,2) (2,1)



'''