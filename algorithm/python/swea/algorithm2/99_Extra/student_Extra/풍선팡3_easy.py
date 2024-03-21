import sys
sys.stdin = open('input.txt')

dx1 = [0,1,0,-1]
dy1 = [1,0,-1,0]
dx2 = [1,1,-1,-1]
dy2 = [-1,1,1,-1]

def balloon_pang(arr):
    max_val = 0
    temps = []
    for x in range(N):
        for y in range(M):
            temp = arr[x][y]
            for i in range(4):
                if arr[x][y] %2 ==0:
                    nx = x + dx1[i]
                    ny = y + dy1[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]

                if temp % 2 == 0 :
                    temps.append(temp)
                elif temp %2 == 0 and len(temps)==1:
                    if max_val < sum(temps):
                        max_val = sum(temps)

                elif arr[x][y] %2 ==1:
                    nx = x + dx2[i]
                    ny = y + dy2[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]
                if temp % 2 == 1:
                    max_val = temp

            if max_val < temp:
                max_val = temp
    return max_val

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    balloons = [list(map(int,input().split())) for i in range(N)]
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {balloon_pang(balloons)}')

