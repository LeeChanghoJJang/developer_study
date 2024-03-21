import sys
sys.stdin = open('input.txt')

dx1 = [0,1,0,-1]
dy1 = [1,0,-1,0]
dx2 = [1,1,-1,-1]
dy2 = [-1,1,1,-1]

def balloon_pang(arr):
    max_val = 0
    for x in range(N):
        for y in range(M):
            temp = arr[x][y]
            if arr[x][y] % 2 == 0:
                for i in range(4):
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]

            elif arr[x][y] %2 ==1:
                for i in range(4):
                    nx = x + dx2[i]
                    ny = y + dy2[i]
                    if 0<=nx<N and 0<=ny<M:
                        temp += arr[nx][ny]
    return max_val

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    balloons = [list(map(int,input().split())) for i in range(N)]
    print(f'#{tc} {balloon_pang(balloons)}')