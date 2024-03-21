import sys
sys.stdin = open('input.txt')
# 시작점 찾기 함수
def start_xy(arr):
    for row in range(16):
        for col in range(16):
            if arr[row][col] =='2':
                return [row,col]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# DFS 함수 구상(백트래킹 활용)
def DFS(start):
    stack = [start]
    while stack:
        x,y = stack[-1]
        visited[x][y]=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<16 and 0<=ny<16 and visited[nx][ny]==0 and arr[nx][ny] !='1':
                visited[nx][ny]=1
                stack.append([nx,ny])
                break
            if arr[nx][ny]=='3':
                return 1
        else:
            stack.pop()
    return 0


for _ in range(1,11):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    start = start_xy(arr)
    print(f'#{tc} {DFS(start)}')