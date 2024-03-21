import sys
sys.stdin = open('input.txt')

dx = [0,1]
dy = [1,0]

def search(x,y):
    stack = [[x,y, data[x][y]]]
    while stack: # 모든 조사 대상 조사 완료할 때까지
        x,y,cnt = stack.pop()
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < N and ny < N:
                '''
                내가 [nx][ny] 번째에 도달하려고 할 때 드는 누적값
                이번 조사에서 쌓아온 누적값이 이전번 누군가가 쌓아온 누적값보다 적은 경우에만
                이동할 수 있도록 
                '''
                if visited[nx][ny] > cnt + data[nx][ny]:
                    visited[nx][ny] = cnt + data[nx][ny]
                    stack.append((nx,ny,cnt+data[nx][ny]))

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    '''
        나중에는, 이곳에 특정 좌표에 도달하는 데 드는 누적값을 기록
        그 누적값들은, 최솟값으로 갱신할 것임
        그럼, 첫 비교대상은 충분히 큰 값이어야 하 
    '''
    visited = [[] * N for _ in range(N)]
    for d in data:
        print(D)
    print()
    # 출력
    print(f'#{tc}')
