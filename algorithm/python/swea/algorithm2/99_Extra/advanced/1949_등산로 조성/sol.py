import sys
sys.stdin = open('input.txt')
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def finds_max():
    max_value = 0
    for i in range(N):
        for j in range(N):
            if max_value < arr[i][j]:
                max_value = arr[i][j]
    return max_value

def bfs(x,y,visited,direction):
    global max_val
    queue = deque([[x,y]])
    visited[x][y]=1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<N and 0<=ny<N:
                if not visited[nx][ny] and arr[x][y] < arr[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx,ny])
                if max_val < visited[nx][ny]:
                    max_val = visited[nx][ny]
    return

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_val = 0
    max_value = finds_max()
    for i in range(N):
        for j in range(N):
            for direction in range(4):
                if arr[i][j] == max_value:
                    bfs(i,j,[[0]*N for _ in range(N)])
    print(f'#{tc} {max_val}')