T = int(input())
from collections import deque
dx = [0,1,0,-1] # 우측 -> 남측
dy = [1,0,-1,0]
def BFS(x,y,visited):
    first_x = x
    first_y = y
    max_nx = 0
    max_ny = 0
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] ==0 and arr[nx][ny] != 0:
                arr[nx][ny]=0
                visited[nx][ny]=1
                queue.append([nx,ny])
                if max_nx < nx:
                    max_nx = nx
                if max_ny < ny:
                    max_ny = ny
    return [max_nx-first_x+1,max_ny-first_y+1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    temp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                temp.append(BFS(i,j,visited))
    temp.sort(key=lambda x: (x[0]*x[1],x[0],x[1]))
    print(f'#{tc} {len(temp)}',end=' ')
    for i,j in temp:
        print(i,j,end=' ')
    print()