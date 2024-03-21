import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]
    x=99
    y=0
    for i in range(100):
        if arr[x][i] ==2:
            y=i
    # 왼, 오, 위 순
    dx = [0,0,-1]
    dy = [-1,1,0]
    visited = [[0] *100 for _ in range(100)]
    while x !=0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<100 and 0<=ny<100 and arr[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny]=1
                x,y=nx,ny
                break
    print(f'#{tc} {y}')
