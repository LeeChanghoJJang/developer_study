import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_rooms(x, y, visited, dp):
    if visited[x][y] != 0:
        return visited[x][y]

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and rooms[nx][ny] == rooms[x][y] + 1:
            visited[x][y] = max(visited[x][y], find_rooms(nx, ny, visited, dp) + 1)

    return visited[x][y]

for tc in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    cnt = 0
    first = float('inf')

    for i in range(N):
        for j in range(N):
            result = find_rooms(i, j, visited, dp)
            if cnt < result or (cnt == result and first > rooms[i][j]):
                cnt = result
                first = rooms[i][j]

    print(f'#{tc} {first} {cnt}')
