import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 시작점 찾기 함수
def find_start(miro,N):
    for i in range(N):
        for j in range(N):
            # 2찾으면 바로 나오기
            if miro[i][j]=='2':
                return [i,j]
# BFS 함수 정의
def BFS(x,y,N):
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                # 방문한 적이 없으며, 길인 경우에만!
                if visited[nx][ny]==0 and miro[nx][ny]=='0':
                    queue.append([nx,ny])
                    visited[nx][ny] += visited[x][y]+1
                # 아묻따 3나오면 무조건 누적된 거리 반환
                elif miro[nx][ny]=='3':
                    return visited[x][y]
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(input()) for _  in range(N)]
    x,y = find_start(miro,N)
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {BFS(x,y,N)}')
