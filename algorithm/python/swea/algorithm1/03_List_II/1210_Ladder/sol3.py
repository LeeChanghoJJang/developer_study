import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N= int(input())
    ladder = [list(map(int, input().split())) for _  in range(100)]

    # 도착점 찾기
    x=99
    y=0
    for i in range(100):
        if ladder[x][i] == 2:
            y=i

    # 델타 검색 이용(좌, 우, 상 순서)
    dx = [0,0,-1]
    dy = [-1,1,0]

    # 방문한 위치 가지 않기 위해 방문행렬 생성
    visited = [[0]*100 for _ in range(100)]

    # x가 0에 도달하기 전까지 반복문 돌리기
    while x != 0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx,ny가 행렬 범위 내에 있고, 방문한 적이 없으면
            if 0<= nx <100 and 0 <= ny <100 and not visited[nx][ny] and ladder[nx][ny]:
                visited[nx][ny] = 1
                x,y = nx,ny
                break
    # 위를 만족하는 nx,ny가 전혀 없다는 뜻이므로,
    else:
        print(f'#{tc} {y}')