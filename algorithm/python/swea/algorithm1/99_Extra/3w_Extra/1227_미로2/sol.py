from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def DFS(miro):
    queue = deque([[1,1]])
    while queue:
        x,y = queue[-1]
        visited[x][y]=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<100 and 0<=ny<100 and miro[nx][ny]!='1' and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append([nx,ny])
                break
            if miro[nx][ny] =='3':
                return 1
        else:
            queue.pop()
    return 0

for _ in range(1,11):
    tc = int(input())
    miro = [input() for _ in range(100)]
    visited = [[0] * 100 for _  in range(100)]
    print(f'#{tc} {DFS(miro)}')