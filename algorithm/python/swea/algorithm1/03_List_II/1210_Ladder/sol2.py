# 재귀 이용

# 좌우상
# 위로 올라가는 경우의 우선순위가 제일 낮기 때문
dx = [0,0,-1]
dy = [-1,1,0]

def search(i,j):
    if x == 0 : # 제일 위에 까지 왔다면
        return y # 그 때의 y값 반환하고 종료
    # 아직 제일 위에까지 못왔으면 계속 조사
    for i in range(3): # 3방향 조사
        nx = x +dx[i]
        ny = y + dy[i]
        if 0<=nx <100 and 0<=ny < 100 and arr[nx][ny] \
            and arr[nx][ny]==1 and not visited[nx][ny]:
            visited[nx][ny]=1
            search(nx,ny)


    # 출발시점의 j좌표 기록
    original_j = j
    while i != 99:  # 탐색 시작 -> i가 99가 될 때 까지
        # 3방향 탐색  아래    왼     오
        for dir in [(1, 0), (0, -1), (0, 1)]:
            # 현재위치 i,j를 기준으로 dir[0],dir[1]
            ni = i + dir[0]  # 다음 탐색 대상 i 좌표값
            nj = j + dir[1]  # 다음 탐색 대상 j 좌표값
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:  # 이동 가능하다.
                if arr[ni][nj]==1:
                    if not visited[ni][nj]:
                        i, j = ni, nj
                        visited[i][j] = 1
                if arr[ni][nj] == 2:
                    return original_j

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    # 방문 표시용 0으로 채워진 2차원 리스트
    visited = [[0] * 100 for _ in range(100)]
    # 최종 결괏값
    result = 0
    for j in range(100):
        # 출발 지점 : i좌표 ==0으로 고정
        if arr[0][j] ==1:
            result = search(0,j)
    print(result)