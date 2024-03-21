import sys
sys.stdin = open('input.txt')

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def find_rooms(x,y,visited):
    result = 0
    stack = [[x,y]]
    first = rooms[x][y]
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<= ny <N and rooms[nx][ny] == rooms[x][y]+1:
                visited[nx][ny] = visited[x][y] + 1
                stack.append([nx,ny])
                if result < visited[nx][ny]:
                    result = visited[nx][ny]
    return first,result

for tc in range(1,int(input())+1):
    N = int(input())
    rooms = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    first = float('inf')
    temp =[]
    for i in range(N):
        for j in range(N):
            second, result = find_rooms(i,j,visited)
            if cnt <= result:
                cnt = result
                temp.append([second,cnt])

    for i,j in sorted(temp):
        if j == cnt:
            first = i
            break
    print(f'#{tc} {first} {cnt+1}')