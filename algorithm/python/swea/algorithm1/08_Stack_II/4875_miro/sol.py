import sys
sys.stdin =open('input.txt')
# 델타 탐색을 위한 델타 설정
dx = [0,1,0,-1]
dy = [-1,0,1,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 주어진 숫자를 2차원 배열로 받기 위한 graph 설정
    graph =[input() for _ in range(N)]
    # 한번 방문한 곳은 재방문하지 않기 위해 visited 리스트 설정
    visited = [[1] * (N + 1) for _ in range(N+1)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '2':
                x,y=[i,j]
                break
    # check는 큰 의미는 없으며, 나중에 중첩 반복문을 깨기 위한 장치
    check=False
    # 찾은 시작점을 temp라는 스택에 저장하고, temp 스택을 활용하여 BFS 이용할 예정
    temp =[[x,y]]
    # 종착점 찾을 때까지 진격
    while temp:
        # temp에서 그 다음 출발할 x,y 선택
        x,y = temp.pop(0)
        # 방문한 곳은 0로 표시
        visited[x][y]=0
        # 사방에 0이 있으면 진격
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 행렬 범위를 초과하지 않는 범위에서 벽이 아닌 경우 진격
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] !='1' and visited[nx][ny] != 0:
                temp.append([nx,ny])
                # 도착점에 도달한 경우, 출력
                if graph[nx][ny]=='3':
                    # 결과값 찾았으므로 1 출력
                    print(f'#{tc} 1')
                    check = True
                    break
        if check:
            break
    # 모든 반복문을 순회하고 나서, temp에 남은 것이 없다면 못찾은 것이므로 0 반환
    if len(temp) == 0:
        print(f'#{tc} 0')







