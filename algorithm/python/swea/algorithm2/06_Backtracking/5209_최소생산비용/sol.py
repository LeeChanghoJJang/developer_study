import sys
sys.stdin = open('input.txt')

def dfs(start,result):
    global min_cost
    if start == N:
        if min_cost > result:
            min_cost = result
        return
    if result > min_cost:
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=1
            dfs(start+1,result+arr[start][i])
            visited[i]=0

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_cost = int(1e9)
    visited = [0] * N
    dfs(0,0)
    print(f'#{tc} {min_cost}')

