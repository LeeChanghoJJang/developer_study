import sys
sys.stdin = open('input.txt')
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]

# 파리채를 내리쳤을 때 때려 죽일 수 있는 파리의 개수
def insectiside(i,j,M):
    result = 0
    visited = [[0] * (N+1) for _ in range(N+1)]
    # 범위를 벗어나지 않을 동안만큼만 파리채에 죽은 파리의 개수를 하나씩 순회
    for x in range(i, min(N,i+M)):
        for y in range(j, min(N,j+M)):
            # 시작점 일단 저장
            if not visited[x][y]:
                result += arr[x][y]
                # 순회할 때마다 그 좌표 방문처리
                visited[x][y]=1
            # 방사능 범위에 있는 파리를 파리채로 쳤을 때
            if [x,y] in paris:
                # 대각선 4방향 전부 탐색
                for plus in range(4):
                    nx = x + dx[plus]
                    ny = y + dy[plus]
                    # 주어진 범위 내고, 중복되지 않았으면 result값에 가산
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        result += arr[nx][ny]
                        visited[nx][ny] = 1
    return result

# 파리영역을 탐색하여 가장 많이 죽였을 때 파리의 개수를 반환하기 위한 함수
def search(arr):
    result = 0
    # 시작점을 기준으로 M*M 배열만큼 파리를 죽일것
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = insectiside(i, j, M)
            if result < kill:
                result = kill
    return result

T = int(input())
for tc in range(1,T+1):
    # N : 파리가 얼마나 있는지, M : 파리채 범위, B : 방사능 파리
    N,M,B = map(int,input().split())
    paris = [list(map(lambda x:int(x)-1,input().split())) for _ in range(B)]
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {search(arr)}')
